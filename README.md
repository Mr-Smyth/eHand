# eHand

![eHand logo](https://i.ibb.co/nL9459P/image.png "Site logo")


[Click here to view eHand](https://mr-smyth-ehand.herokuapp.com/)


***"Time is the most valuable thing a man can spend. – Theophrastus...."***

Time is indeed a very, very precious comodity - perhaps the most precious. Time given to others is a wonderful gift and its time you cannot get back!  
Actually, thats not technically true, because now you can, with eHand.

eHand is a site where users can visit to ask for help, or provide it. Free members are able to browse a selection of notices by premium members 
and can offer their help.
Premium members can also offer their help and can also create notices - looking for any sort of a hand.   
Premium members can also use the sites unique currency - TIME as payment for any help provided. In doing so, you can actually get Time back.   

This website is not restricted to individuals, it can be easily extended to include community groups, offer incentives to those who help out in their communities
and provide a means to those without.

eHand will be submitted as my MS4 and final project in my Full Stack Software Development diploma.

# UX

## Purpose

eHand allows members to create a post for some form of help that they need, this can be absolutly anything.   
It allows other members to view and respond by offering to help - ***or commit*** - to the member who posted. The member who creates the post 
will also include the time/duration of the task, and this is important as this represents the amount of the TIME payment available.   

You see i believe the most precious thing we spend today is time - and to give that time to someone, freely - to help them out, is a 
wonderful gift.   

Now we've all been there - Someone helps you out - you maybe offer them money as you want to show your gratittude - 
mostly it is turned down, with a friendly - get me again!

Wouldent it be nice if you could give back what they so freely gave? - which is their own TIME.  
Enabling them to use that TIME as a form of currency to purchase someone else's TIME - and get something done that they need?
Perhaps their car needs brakes fitted or their daughter needs help with her Maths - with TIME
they can get whatever it is they need.   

I really cant think of a greater Gift - than the gift of TIME!   

So therefore i came up with the idea of creating time on the site, as a token payment system.
To be included in the payment system - you must be a premium member, this requires registering for a eHand account and then 
selecting the premium membership type in the upgrade section, or by clicking Discover Premium in your profile.  
This provides the user with a Time Account - with a balance of 10t ***(t = the time unit currency on site, equivelent to hours)***  

The helping doesnt stop there. All profits created from membership subscriptions will be donated to a different charity each month.
Future planned incentives to be included are rewarding Time payments to members giving help with organised charity events.   





## Goals

### Visitor Goals

The target audience are:
+ People of all ages who need help with a task.
+ People who have not means to pay for professional help.
+ Groups and organisations looking for an interesting way to encourage/incentivise people to help out and get involved in events.
+ To create a public platform that promotes helping others - and yet still gives something back.   

### Member Goals

The Goals for members are:
+ Get help with with a task or event by posting a notice.
+ Provides a way for people to help out, by reading the notices and responding.
+ A method of accumulating TIME, by helping another member.
+ A method of getting "***stuff***" done - by a method almost similar to bartering, where you trade Time for Time.   

### Business Goals

The Goals as a business are:

+ To create a large community of members to provide a diverse mix of talents.
+ To create a large community of members to build a substantial subscription income - which will be passed onto charity.


## User Stories

1.  As a non member: I want to visit the sites homepage	and get a clear overview of what the site does and how i can sign up.
2.  As a Free member i want to be able to sign in to eHand and view Posts and offer help
3.  As a premium member when i create my membership, i want to know my payment donates to charity
4.  As a premium member when i create my membership, i want to be awarded the 2 free hours of time to spend on the site.
5.  As a premium member i want to be able to create a posting/ or hand.
6.  As a Premium member i want other members to be able to see my post/hand - and offer help.
7.  As a premium member i want to be able to offer my help to others.
8.  As a premium member i want to be able to transfer my time to another member who helped me.
9.  As a premium member i want to be able to accept payment of time from a member i helped. 
10. As a premium member i want to get a notification when i log in - if another member has offered help
11. As a member i want a way to communicate to a member who is offering help, or if i am offering it.
12. As a member i would like to see commitments i have made in my profile
13. As a member i would like to see my notices in my profile.

---   


# UI

eHand will use the Bootstrap framework to create a clean uncluttered intuitive layout. 
The layout will be responsive having been built from a mobile first perspective.   
The Navbar is positioned down the page 200px as a default position - and will retreat to a fixed position, by way of some custom JavaScript, to
 the top of the page allowing content to dissappear underneath it when the user scrolls.   
 The navbar will be almost focal, clean crisp and simple, with a very simple lime green glow and gradient hover effect
reverting to the simpler ghost white when not being interacted with.

The logo and choice of colours was to achieve a nice contrast between a grey hand background image and the lime green colour.
The logo was designed with pastel type colours, so its visable when needed - but not to take over the page.

## Colours:

I choose a green and grey mix, as i find them an unusual, yet comfortable mix of colours. The grey, can obviously be dull, but i find that the slightest touches
of a ***Wow*** colour such as the lime green, give a wonderful contrast that lifts the page.
Other bootstrap standard colours are used in places where the lime green would have been too overpowering.

*   [Ghost-white(#f8f8ff)](https://www.color-hex.com/color/f8f8ff) - will be used for windowed areas.
*   [#555555](https://www.color-hex.com/color/555555) -  as the main font colour
*   [lime green(#c2fa00)](https://www.color-hex.com/color/c2fa00) - used in all areas for text, borders, highlighting etc.  


## Fonts

The font chosen for this site is Nunito. I liked the clear simple rounded style, which fitted with the simple clean feel of the planned site.

## Styling

Rounded corners and gentle hover effect shading along with fade-in elements were deliberate to give a smooth relaxed feel
to the visitor as each page gently fades into view.   
A current username or logged in status, deliberatly styled to be subtle, is positioned oposite the logo, just to indicate current logged in status.   
The site logo retreats from view when page is scrolled, returning with the lowered navbar when page is scrolled to the top.


## Wireframes

[Home Page: ](https://github.com/Mr-Smyth/eHand/blob/master/docs/wireframes/home-wireframe.pdf)   
[Register Page: ](https://github.com/Mr-Smyth/eHand/blob/master/docs/wireframes/register-wireframe.pdf)   
[Sign In Page: ](https://github.com/Mr-Smyth/eHand/blob/master/docs/wireframes/sign-in-wireframe.pdf)   
[Upgrade Page: ](https://github.com/Mr-Smyth/eHand/blob/master/docs/wireframes/upgrade-wireframe.pdf)   
[Create a Notice: ](https://github.com/Mr-Smyth/eHand/blob/master/docs/wireframes/create-notice-wireframe.pdf)   
[Notices: ](https://github.com/Mr-Smyth/eHand/blob/master/docs/wireframes/notices-wireframe.pdf)   
[Profile Page: ](https://github.com/Mr-Smyth/eHand/blob/master/docs/wireframes/profile-wireframe.pdf)   
[Profile - My Notices: ](https://github.com/Mr-Smyth/eHand/blob/master/docs/wireframes/my-notices-wireframe.pdf)   
[Profile - Commitments: ](https://github.com/Mr-Smyth/eHand/blob/master/docs/wireframes/commitments-wireframe.pdf)   



# Features 

![Home](https://i.ibb.co/VppdCnw/image.png "Home Page example")  

## Existing Features

### Common site elements

#### Logo
Designed by myself, plays on the name using distorted lines from a lowercase letter 'e', to form the likeness of a hand. 
The colours are a Kaki type [green](https://www.color-hex.com/color/6B7365)  and a pastel [indigo/grey](https://www.color-hex.com/color/656573)
to form the text part of the logo. The logo was created using [Paint dot net](https://www.getpaint.net/features.html).

#### A Navbar

Common to every page, the same navbar styling will be applied it will only show links relevant to the users login status.  
An additional navbar is included in the Profile section, to allow simple navigation to important information such as the users commitments and the users own notices.

![NavBar](https://i.ibb.co/nwgn9wB/image.png "NavBar")

#### Information area

Common styling of ghost white and grey font will be applied, with a faint lime green border, matching the rest of the site. 
Page headings when required will be in [lime green(#c2fa00)](https://www.color-hex.com/color/c2fa00), providing clarity to the user.

#### Footer
A common footer with social media links will also the bottom of the page. Hovering reveals individual colours relevant to each link.   

![Footer](https://i.ibb.co/m6m9hVM/image.png "Footer section")


### Home Page

 

Site common styled containers gently fade into view on scrolling. The top 3 containers provide the user with a brief, what, why and how about eHand. 
These containers also provide links to read more on that particular subject. Clicking on this will take the user down to a further reading, information section
with an action button to get started.   
Clicking on get started brings the user to the membership uggrade page, if the user is not signed in, the user will be taken to the sign in page, with option
to register if a new user.



### Notices page

The notices page is the only page, other than the home page, which a non authenticated user can access. 
It displays the complete listing of notices in a paginated view.   

![Notice](https://i.ibb.co/mcVvf7J/image.png "Notice example")    

The Notice displays the bare bones of the requested task, clicking on the details button will take the user to a more detailed page to display
the complete details of the notice, with a comments section for further questions.   
A Premium or Free member may click details and interact in any way possible with the notice, including committing to help the author of the notice.   

A non logged in member is unable to access the details and can only view the notice summary - seen in the image above. The Details button does remain though for the un-logged in visitor to see and possibly click on
and if they do click on Details they will be routed to the Sign In Page.


### Create Notice page

Reachable from the the notices page via a link at the top of the page.

This link is only available for Premium members and will not be visable to Free or non members. Attempting to gain entry via the url, will result in a 403 - Forbidden.

The create Notice page features a form with which the member can fill in the details of the help they require, and then submit the form to post it as a notice in the Notices section of the site. 
The member will also be able to view and edit this notice from their own commitments page within their Profile section.   
By default all notices are linked to the correct author.


### Notice Details page

This page is reachable by clicking on the Details button on a notice. There are a few situations where the Details button is not able to be clicked on:

+ If the visitor is not a authorized member of eHand.
+ If the Notice has already been committed to by another member.

Once in the Details of a Notice, you will see 2 containers. The first container holds all the details entered for the notice, along with some 
relevant action buttons.
The 2nd container contains a comments section enabling communication of querys between author and members interested in helping.

![Details](https://i.ibb.co/J38rTSs/image.png "Notice Details example")  


### Profile

The profile main page holds the details of the member signed in. If entered it will display all the users information, if they have chosen to enter it.
A user can click on the Edit Profile button in the profile information section to edit their profile.   

If the member viewing the page is a Premium Member, then their TIME Account balance is displayed.   

To the right of the profile information is the members current Membership status, and an action button to act on this.

![Profile](https://i.ibb.co/2jyp7kS/image.png "Example profile page")


### My Commitments

Reachable from the profile page. The My Commitments page holds a copy of all the notices the current member has committed to. Each notice is displayed with full details.
An option to remove commitment to a notice is at the bottom of each notice.

### My Notices

Reachable from the profile page. The My Notices page displays all the current notices that the current member has created. An option to update the notice or 
delete it is available in this view at the bottom of each notice

# Tech

*   Django
*   Python3
*   Javascript
*   CSS
*   HTML5
*   Bootstrap
*   Google Fonts
*   Favicons


 and the home page information section has a background with a varied degree of opacity to 
remove the dullness that i felt a solid grey background was giving. This keeps the users attention on the information,
while also providing a nice clouded experience of the background as they scroll.



### Free Members:
Can login to eHand and view posts and offer their help and give it. But they do not have a Time account where they can accept 
Time as payment. They also cannot create posts.

### Premium Members:
Must sign up to the membership deal, which is €5 per month. This money goes to a charity organization and the user is then given 2 Hours of Time in their Time account.
They are able to view and create posts, and offer help to other members posts. They are also able to make and receive Time payments for work done.