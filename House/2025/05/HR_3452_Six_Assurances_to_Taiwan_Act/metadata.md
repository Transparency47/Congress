# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3452?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3452
- Title: Six Assurances to Taiwan Act
- Congress: 119
- Bill type: HR
- Bill number: 3452
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2026-05-20T08:08:35Z
- Update date including text: 2026-05-20T08:08:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-15 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-15 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3452",
    "number": "3452",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "K000391",
        "district": "8",
        "firstName": "Raja",
        "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
        "lastName": "Krishnamoorthi",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Six Assurances to Taiwan Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:35Z",
    "updateDateIncludingText": "2026-05-20T08:08:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-05-15T14:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-15T14:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "NY"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "AZ"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "IA"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "PA"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "CA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "MA"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "WA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CA"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "IL"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "GU"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "WA"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "IN"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "TX"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "NY"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "OH"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "IA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "NY"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "WA"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "NJ"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "HI"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "NY"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "MD"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "UT"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "NY"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3452ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3452\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Krishnamoorthi (for himself, Mr. Meeks , Mr. Stanton , Mrs. Kim , Mr. Nunn of Iowa , and Ms. Malliotakis ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on Rules , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo codify the Six Assurances to Taiwan, provide congressional review of the Six Assurances, protect Taiwan from coercion, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Six Assurances to Taiwan Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nTaiwan is a free and prosperous democracy of more than 23,000,000 people and an important economic partner to the United States.\n**(2)**\nThe People\u2019s Republic of China (PRC) has long sought to subjugate Taiwan and has not renounced the use of force to do so.\n**(3)**\nThe United States longstanding One-China Policy, which is guided by the Taiwan Relations Act, the three United States-China Joint Communiqu\u00e9s, and the Six Assurances, has guided United States-Taiwan relations across successive administrations and contributed to peace and stability in the Indo-Pacific.\n**(4)**\nFrom July to August 1982, before and immediately after the release of the United States-China Joint Communiqu\u00e9 on United States Arms Sales to Taiwan ( the 1982 Joint Communiqu\u00e9 ) on August 17, 1982, the Reagan Administration articulated six key foreign policy principles regarding United States-Taiwan relations.\n**(5)**\nOn July 10, 1982, then-Under Secretary of State Lawrence Eagleburger sent a cable to James Lilley, then-director of the American Institute in Taiwan, detailing what the United States had not agreed to in its negotiations with the People\u2019s Republic of China over the 1982 Joint Communiqu\u00e9. He wrote\u2014\n**(A)**\nWe have not agreed to set a date certain for ending arms sales to Taiwan ;\n**(B)**\nWe have not agreed to prior consultation on arms sales ;\n**(C)**\nWe have not agreed to any mediation role for the U.S. ;\n**(D)**\nWe have not agreed to revise the Taiwan Relations Act ;\n**(E)**\nWe have not agreed to take any position regarding sovereignty over Taiwan ; and\n**(F)**\nThe PRC has at no time urged us to put pressure on Taiwan to negotiate with the PRC; however, we can assure you that we will never do so .\n**(6)**\nOn August 17, 1982, then-Secretary of State Geroge Shultz provided Lilley with a version of the Six Assurances for Taiwan\u2019s government to release, stating that the United States\u2014\n**(A)**\nhas not agreed to set a date for ending arms sales to Taiwan ;\n**(B)**\nhas not agreed to consult with the PRC on arms sales to Taiwan ;\n**(C)**\nwill not play any mediation role between Taipei and Beijing ;\n**(D)**\nhas not agreed to revise the Taiwan Relations Act ;\n**(E)**\nhas not altered its position regarding sovereignty over Taiwan ; and\n**(F)**\nwill not exert pressure on Taiwan to enter into negotiations with the PRC .\n**(7)**\nOn August 17, 1982, then-Assistant Secretary of State for East Asian and Pacific Affairs John H. Holdridge testified on behalf of the executive branch before the Senate Committee on Foreign Relations about the 1982 Joint Communiqu\u00e9 that\u2014\n**(A)**\n[W]e did not agree to set a date certain for ending arms sales to Taiwan ;\n**(B)**\n[The 1982 Joint Communiqu\u00e9] should not be read to imply that we have agreed to engage in prior consultations with Beijing on arms sales to Taiwan ;\n**(C)**\n[W]e see no mediation role for the United States ;\n**(D)**\nWe have no plans to seek any such revisions [to the Taiwan Relations Act] ;\n**(E)**\n[T]here has been no change in our longstanding position on the issue of sovereignty over Taiwan ; and\n**(F)**\n[N]or will we attempt to exert pressure on Taiwan to enter into negotiations with the PRC .\n**(8)**\nOn August 18, 1982, Holdridge testified on behalf of the executive branch before the House Committee on Foreign Affairs about the 1982 Joint Communiqu\u00e9 that\u2014\n**(A)**\n[W]e did not agree to set a date certain for ending arms sales to Taiwan ;\n**(B)**\n[The 1982 Joint Communiqu\u00e9] should not be read that we have agreed to engage in prior consultations with Beijing on arms sales to Taiwan ;\n**(C)**\n[W]e see no mediation role for the United States ;\n**(D)**\nWe have no plans to seek any such revisions [to the Taiwan Relations Act] ;\n**(E)**\n[T]here has been no change in our longstanding position on the issue of sovereignty over Taiwan ; and\n**(F)**\n[N]or will we attempt to exert pressure on Taiwan to enter into negotiations with the People\u2019s Republic of China .\n**(9)**\nThese six foreign policy principles, as articulated by Eagleburger, Shultz, and Holdridge, have collectively come to be known as the Six Assurances.\n**(10)**\nThe House of Representatives and Senate passed a concurrent resolution reaffirming the Taiwan Relations Act and the Six Assurances as cornerstones of United States-Taiwan relations on May 16, 2016, and July 6, 2016, respectively.\n**(11)**\nThe Asia Reassurance Initiative Act of 2018 ( Public Law 115\u2013409 ) states that it is the policy of the United States to faithfully enforce all existing United States Government commitments to Taiwan, consistent with the Taiwan Relations Act of 1979 ( Public Law 96\u20138 ), the [three Joint Communiqu\u00e9s], and the Six Assurances .\n**(12)**\nThe National Defense Authorization Acts for Fiscal Years 2019 through 2025 (Public Laws 115\u2013232, 116\u2013283, 116\u201392, 117\u201381, 117\u2013263, 118\u201331, and 118\u2013159) each recognized the importance of the Six Assurances to United States-Taiwan relations.\n**(13)**\nThe Taiwan Assurance Act of 2020 ( Public Law 116\u2013260 ) states that [i]t is the policy of the United States to reinforce its commitments to Taiwan under the Taiwan Relations Act in a manner consistent with the Six Assurances and in accordance with the United States One China policy .\n#### 3. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe maintenance of peace and stability across the Taiwan Strait is in the political, security, and economic interests of the United States and is a matter of international concern;\n**(2)**\nany unilateral change to the status quo from either side or negotiated settlement of the question of Taiwan\u2019s status without the consent of both sides of the Strait is unacceptable;\n**(3)**\nthe future of Taiwan must be determined by peaceful means; and\n**(4)**\nthe maintenance of the Six Assurances constitutes a stabilizing and necessary component of United States policy toward Taiwan.\n#### 4. Statement of policy\nIt is the policy of the United States to reaffirm that, in the context of the 1982 Joint Communiqu\u00e9, the United States\u2014\n**(1)**\ndid not agree to set a date for ending arms sales to Taiwan;\n**(2)**\ndid not agree to consult with the People\u2019s Republic of China on arms sales to Taiwan;\n**(3)**\ndid not and will not agree to play any mediation role;\n**(4)**\ndid not agree to revise the Taiwan Relations Act;\n**(5)**\ndid not take any position regarding the issue of sovereignty over Taiwan; and\n**(6)**\nwill not exert pressure on Taiwan to enter into negotiations with the People\u2019s Republic of China.\n#### 5. Congressional review of certain actions relating to the Six Assurances to Taiwan\n##### (a) Submission to congress of proposed action\n**(1) In general**\nNotwithstanding any other provision of law, before taking any action described in paragraph (2), the President shall submit to the appropriate congressional committees and leadership a notification that describes the proposed action and the reasons for that action.\n**(2) Actions described**\n**(A) In general**\nAn action described in this paragraph is an action\u2014\n**(i)**\nto pause or terminate the provision of arms of a defensive character to Taiwan;\n**(ii)**\nto negotiate with the People\u2019s Republic of China about the provision of arms of a defensive character to Taiwan;\n**(iii)**\nto mediate between Taiwan and the People\u2019s Republic of China regarding the issue of sovereignty over Taiwan;\n**(iv)**\nto change the United States longstanding position on the issue of the sovereignty over Taiwan; or\n**(v)**\nto exert pressure on Taiwan to enter into negotiations with the People\u2019s Republic of China.\n**(3) Description of type of action**\nEach notification submitted under paragraph (1) with respect to an action described in paragraph (2) shall include a description of whether the action is or is not intended to significantly alter United States foreign policy with respect to Taiwan or the People\u2019s Republic of China.\n**(4) Inclusion of additional matter**\nEach notification submitted under paragraph (1) that relates to an action that is intended to significantly alter United States foreign policy with respect to Taiwan or the People\u2019s Republic of China shall include a description of\u2014\n**(A)**\nthe significant alteration to United States foreign policy with respect to Taiwan or the People\u2019s Republic of China;\n**(B)**\nthe anticipated effect of the action on the economic and national security interests of the United States; and\n**(C)**\nthe anticipated effect of the action on the issue of the sovereignty over Taiwan.\n##### (b) Period for review by congress\n**(1) In general**\nDuring the period of 30 calendar days beginning on the date on which the President submits a notification under subsection (a)(1), the appropriate congressional committees should hold hearings and briefings and otherwise obtain information in order to fully review the notification.\n**(2) Exception**\nThe period for congressional review under paragraph (1) of a notification required to be submitted under subsection (a)(1) shall be 60 calendar days if the notification is submitted on or after July 10 and on or before September 7 in any calendar year.\n**(3) Limitation on actions during initial congressional review period**\nNotwithstanding any other provision of law, during the period for congressional review provided for under paragraph (1) of a notification submitted under subsection (a)(1) proposing an action described in subsection (a)(2), including any additional period for such review as applicable under the exception provided in paragraph (2), neither the President nor any other officer or employee of the United States may expend any appropriated funds in furtherance of that action unless a joint resolution of approval with respect to that action is enacted in accordance with subsection (c).\n**(4) Limitation on actions during presidential consideration of a joint resolution of disapproval**\nNotwithstanding any other provision of law, if a joint resolution of disapproval relating to a notification submitted under subsection (a)(1) proposing an action described in subsection (a)(2) passes both Houses of Congress in accordance with subsection (c), neither the President nor any other officer or employee of the United States may expend any appropriated funds in furtherance of that action for a period of 12 calendar days after the date of passage of the joint resolution of disapproval.\n**(5) Limitation on actions during congressional reconsideration of a joint resolution of disapproval**\nNotwithstanding any other provision of law, if a joint resolution of disapproval relating to a notification submitted under subsection (a)(1) proposing an action described in subsection (a)(2) passes both Houses of Congress in accordance with subsection (c), and the President vetoes the joint resolution, neither the President nor any other officer or employee of the United States may take that action or expend any appropriated funds in furtherance of that action for a period of 10 calendar days after the date of the President\u2019s veto.\n**(6) Effect of enactment of a joint resolution of disapproval**\nNotwithstanding any other provision of law, if a joint resolution of disapproval relating to a notification submitted under subsection (a)(1) proposing an action described in subsection (a)(2) is enacted in accordance with subsection (c), neither the President nor any other officer or employee of the United States may take that action or expend any appropriated funds in furtherance of that action.\n##### (c) Joint resolutions of disapproval or approval\n**(1) Definitions**\nIn this subsection:\n**(A) Joint resolution of approval**\nThe term joint resolution of approval means only a joint resolution of either House of Congress\u2014\n**(i)**\nthe title of which is as follows: A joint resolution approving the President\u2019s proposal to take an action relating to the Six Assurances to Taiwan. ; and\n**(ii)**\nthe sole matter after the resolving clause of which is the following: Congress approves of the action relating to the action with respect to the Six Assurances to Taiwan proposed by the President in the notification submitted to Congress under section 2(a)(1) of the Six Assurances to Taiwan Act on _______ relating to ________. , with the first blank space being filled with the appropriate date and the second blank space being filled with a short description of the proposed action.\n**(B) Joint resolution of disapproval**\nThe term joint resolution of disapproval means only a joint resolution of either House of Congress\u2014\n**(i)**\nthe title of which is as follows: A joint resolution disapproving the President\u2019s proposal to take an action relating to the Six Assurances to Taiwan. ; and\n**(ii)**\nthe sole matter after the resolving clause of which is the following: Congress disapproves of the action relating to the Six Assurances to Taiwan proposed by the President in the notification submitted to Congress under section 2(a)(1) of the Six Assurances to Taiwan Act on _______ relating to ________. , with the first blank space being filled with the appropriate date and the second blank space being filled with a short description of the proposed action.\n**(2) Introduction**\nDuring the period of 30 calendar days provided for under subsection (b)(1), including any additional period as applicable under the exception provided in subsection (b)(2), a joint resolution of approval or joint resolution of disapproval may be introduced\u2014\n**(A)**\nin the House of Representatives, by the majority leader or the minority leader; and\n**(B)**\nin the Senate, by the majority leader (or the majority leader\u2019s designee) or the minority leader (or the minority leader\u2019s designee).\n**(3) Floor consideration in house of representatives**\nIf the appropriate congressional committee of the House of Representatives has not reported the joint resolution within 10 legislative days after the date of referral, that committee shall be discharged from further consideration of the joint resolution.\n**(4) Consideration in the senate**\n**(A) Committee referral**\nA joint resolution of approval or joint resolution of disapproval introduced in the Senate shall be referred to the Committee on Foreign Relations.\n**(B) Reporting and discharge**\nIf the committee to which a joint resolution of approval or joint resolution of disapproval was referred has not reported the joint resolution within 10 calendar days after the date of referral of the joint resolution, that committee shall be discharged from further consideration of the joint resolution and the joint resolution shall be placed on the appropriate calendar.\n**(C) Proceeding to consideration**\nNotwithstanding Rule XXII of the Standing Rules of the Senate, it is in order at any time after the Committee on Foreign Relations reports a joint resolution of approval or joint resolution of disapproval to the Senate or has been discharged from consideration of such a joint resolution (even though a previous motion to the same effect has been disagreed to) to move to proceed to the consideration of the joint resolution, and all points of order against the joint resolution (and against consideration of the joint resolution) are waived. The motion to proceed is not debatable. The motion is not subject to a motion to postpone. A motion to reconsider the vote by which the motion is agreed to or disagreed to shall not be in order.\n**(D) Rulings of the chair on procedure**\nAppeals from the decisions of the Chair relating to the application of the rules of the Senate, as the case may be, to the procedure relating to a joint resolution of approval or joint resolution of disapproval shall be decided without debate.\n**(E) Consideration of veto messages**\nDebate in the Senate of any veto message with respect to a joint resolution of approval or joint resolution of disapproval, including all debatable motions and appeals in connection with the joint resolution, shall be limited to 10 hours, to be equally divided between, and controlled by, the majority leader and the minority leader or their designees.\n**(5) Rules relating to senate and house of representatives**\n**(A) Treatment of senate joint resolution in house**\nIn the House of Representatives, the following procedures shall apply to a joint resolution of approval or a joint resolution of disapproval received from the Senate (unless the House has already passed a joint resolution relating to the same proposed action):\n**(i)**\nThe joint resolution shall be referred to the appropriate committee.\n**(ii)**\nIf a committee to which a joint resolution has been referred has not reported the joint resolution within 5 legislative days after the date of referral, that committee shall be discharged from further consideration of the joint resolution.\n**(iii)**\nBeginning on the third legislative day after each committee to which a joint resolution has been referred reports the joint resolution to the House or has been discharged from further consideration thereof, it shall be in order to move to proceed to consider the joint resolution in the House. All points of order against the motion are waived. Such a motion shall not be in order after the House has disposed of a motion to proceed on the joint resolution. The previous question shall be considered as ordered on the motion to its adoption without intervening motion. The motion shall not be debatable. A motion to reconsider the vote by which the motion is disposed of shall not be in order.\n**(iv)**\nThe joint resolution shall be considered as read. All points of order against the joint resolution and against its consideration are waived. The previous question shall be considered as ordered on the joint resolution to final passage without intervening motion except 2 hours of debate equally divided and controlled by the sponsor of the joint resolution (or a designee) and an opponent. A motion to reconsider the vote on passage of the joint resolution shall not be in order.\n**(B) Treatment of house joint resolution in senate**\n**(i) Receipt before passage**\nIf, before the passage by the Senate of a joint resolution of approval or joint resolution of disapproval, the Senate receives an identical joint resolution from the House of Representatives, the following procedures shall apply:\n**(I)**\nThat joint resolution shall not be referred to a committee.\n**(II)**\nWith respect to that joint resolution\u2014\n**(aa)**\nthe procedure in the Senate shall be the same as if no joint resolution had been received from the House of Representatives; but\n**(bb)**\nthe vote on passage shall be on the joint resolution from the House of Representatives.\n**(ii) Receipt after passage**\nIf, following passage of a joint resolution of approval or joint resolution of disapproval in the Senate, the Senate receives an identical joint resolution from the House of Representatives, that joint resolution shall be placed on the appropriate Senate calendar.\n**(iii) No companion measure**\nIf a joint resolution of approval or a joint resolution of disapproval is received from the House, and no companion joint resolution has been introduced in the Senate, the Senate procedures under this subsection shall apply to the House joint resolution.\n**(C) Application to revenue measures**\nThe provisions of this paragraph shall not apply in the House of Representatives to a joint resolution of approval or joint resolution of disapproval that is a revenue measure.\n**(6) Rules of house of representatives and senate**\nThis subsection is enacted by Congress\u2014\n**(A)**\nas an exercise of the rulemaking power of the Senate and the House of Representatives, respectively, and as such is deemed a part of the rules of each House, respectively, and supersedes other rules only to the extent that it is inconsistent with such rules; and\n**(B)**\nwith full recognition of the constitutional right of either House to change the rules (so far as relating to the procedure of that House) at any time, in the same manner, and to the same extent as in the case of any other rule of that House.\n##### (d) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(2)**\nthe Committee on Foreign Relations of the Senate.\n#### 6. Severability\nIf any provision of this Act, or the application thereof, is held invalid, the validity of the remainder of this Act and the application of such provision to other persons and circumstances shall not be affected thereby.",
      "versionDate": "2025-05-15",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-11-19",
        "text": "Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "3208",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Six Assurances to Taiwan Act",
      "type": "S"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-06-20T13:53:49Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3452ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Six Assurances to Taiwan Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Six Assurances to Taiwan Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To codify the Six Assurances to Taiwan, provide congressional review of the Six Assurances, protect Taiwan from coercion, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T03:48:17Z"
    }
  ]
}
```
