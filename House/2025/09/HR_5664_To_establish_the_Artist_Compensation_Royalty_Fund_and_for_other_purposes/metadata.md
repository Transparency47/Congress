# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5664?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5664
- Title: Living Wage for Musicians Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5664
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2026-01-10T09:06:28Z
- Update date including text: 2026-01-10T09:06:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5664",
    "number": "5664",
    "originChamber": "House",
    "policyArea": {
      "name": "Arts, Culture, Religion"
    },
    "sponsors": [
      {
        "bioguideId": "T000481",
        "district": "12",
        "firstName": "Rashida",
        "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
        "lastName": "Tlaib",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Living Wage for Musicians Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-10T09:06:28Z",
    "updateDateIncludingText": "2026-01-10T09:06:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NJ"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "MN"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "IL"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "MS"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "PA"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5664ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5664\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Ms. Tlaib (for herself, Mrs. McIver , Ms. Ocasio-Cortez , Ms. Omar , Mrs. Ramirez , and Mr. Thompson of Mississippi ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo establish the Artist Compensation Royalty Fund, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Living Wage for Musicians Act of 2025 .\n#### 2. Artist Compensation Royalty Fund\n##### (a) Establishment\n**(1) In general**\nThe Register, with the approval of the Librarian of Congress, shall designate an eligible entity to establish and administer a fund to be known as the Artist Compensation Royalty Fund.\n**(2) Notice of designation in Federal Register**\nNot later than 30 days after the eligible entity is designated under paragraph (1), the Register shall publish a notice in the Federal Register that\u2014\n**(A)**\nincludes the contact information for the eligible entity; and\n**(B)**\nthe reason for why the Register designated the eligible entity under such paragraph.\n##### (b) Deposit of amounts into Fund\n**(1) Deposit**\nThe Fund Administrator shall deposit into the Fund any amounts received by the Fund Administrator under paragraph (2) or (3).\n**(2) Amounts from service providers**\nNot later than the last day of the first calendar quarter after the calendar quarter in which the Fund Administrator is designated, and each calendar quarter thereafter, a service provider shall provide to the Fund Administrator, for deposit into the Fund\u2014\n**(A)**\nthe amounts collected by the service provider in the prior calendar quarter from the living wage royalty fee; and\n**(B)**\n10 percent of any non-subscription revenue received by the service provider in the prior calendar quarter.\n**(3) Amounts from sources other than service providers**\nThe Fund Administrator may receive amounts for deposit into the Fund from any source, including from a Federal, State, or local government.\n##### (c) Use of Fund\nAmounts in the Fund shall be made available in accordance with section 3.\n#### 3. Payments to musical artists from Artist Compensation Royalty Fund\n##### (a) In general\n**(1) Allocation of payments**\nAmounts in the Fund shall be allocated as follows:\n**(A)**\n90 percent of such amounts shall be allocated for payments to eligible featured artists.\n**(B)**\n10 percent of such amounts shall be allocated for payments to eligible non-featured artists.\n**(2) Payments from Fund**\nNot later than the last day of the calendar quarter in which amounts are first deposited into the Fund under section 2(b)(2), and once each calendar quarter thereafter, the Fund Administrator shall promptly provide\u2014\n**(A)**\na percentage of the amount allocated under paragraph (1)(A) of this subsection to each eligible featured artist, that is equal to the percentage of qualifying streams accrued by the eligible featured artist in the prior calendar quarter out of all qualifying streams accrued by all eligible featured artists in the prior calendar quarter; and\n**(B)**\npayment from the amount allocated under paragraph (1)(B) of this subsection to the American Federation of Musicians and Screen Actors Guild and the American Federation of Television and Radio Artists Intellectual Property Rights Distribution Fund (or any successor Fund) for distribution to each eligible non-featured artist.\n**(3) Unclaimed funds**\nIf the Fund Administrator attempts to the best of the ability of the Fund Administrator to identify an eligible featured artist to provide payment to such artist under paragraph (2)(A), and is unable to identify such artist at such time, the Fund shall\u2014\n**(A)**\nretain the required payment in a segregated trust account; and\n**(B)**\nif the Fund Administrator is not able to identify such artist after a period determined reasonable by the Fund Administrator, deposit the payment back into the Fund.\n##### (b) Retention of records\nThe Fund Administrator shall\u2014\n**(1)**\nkeep books and records relating to\u2014\n**(A)**\namounts provided to the Fund Administrator under section 2(b)(2); and\n**(B)**\namounts distributed from the Fund under subsection (a) of this section; and\n**(2)**\nretain any such book or record for a period of not less than 3 calendar years after the date on which such book or record is created.\n#### 4. Service Provider Obligations\n##### (a) Living wage royalty fee\nBeginning on a date determined appropriate by the Fund Administrator, the service provider shall charge each person charged a subscription fee by the service provider an additional fee in an amount equal to 50 percent of the subscription fee charged by the service provider, except that such additional fee shall not be an amount less than $4 or more than $10.\n##### (b) Notice of additional fee\nIn each statement or receipt a service provider provides for the charge of a subscription fee and the additional fee required by subsection (a), the service provider shall include a line item describing such additional fee.\n##### (c) Treatment of royalty\nA service provider may not include the amounts collected by the service provider from the living wage royalty fee in any calculation by the service provider of the total costs or revenue of content for the service provider.\n##### (d) Records\n**(1) Retention**\nBeginning on the date on which the Fund Administrator is designated\u2014\n**(A)**\neach service provider shall keep books and records relating to activities carried out by the service provider under this Act; and\n**(B)**\nretain such book and records for a period of not less than 3 calendar years after the date on which such book or record is created.\n**(2) Regulations**\nThe Fund Administrator may\u2014\n**(A)**\nrequire, by regulation, that service providers provide the Fund Administrator information on\u2014\n**(i)**\nnon-subscription revenue received by the service provider;\n**(ii)**\nrevenue received by the service provider from subscription fee;\n**(iii)**\nthe collection of the living wage royalty fee by the service provider; and\n**(iv)**\ndata of the service provider with respect to the number streams accrued by artists through such service provider; and\n**(B)**\naudit the books and records of a service provider to verify any information provided by that service provider under subparagraph (A).\n#### 5. Enforcement\nThe Fund Administrator may establish, by regulation, penalties for\u2014\n**(1)**\na violation of a prohibition under this Act by a service provider; or\n**(2)**\na failure to comply with a requirement under this Act by a service provider.\n#### 6. Definitions\nIn this Act:\n**(1) Artist**\nThe term artist \u2014\n**(A)**\nmeans a human creator; and\n**(B)**\ndoes not include\u2014\n**(i)**\ncorporate entities; or\n**(ii)**\nfully generative artificial intelligence.\n**(2) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na single non-profit entity that is\u2014\n**(i)**\nestablished solely for the purpose of establishing and administering the Fund;\n**(ii)**\ngoverned by a Board of Directors that includes\u2014\n**(I)**\ncommittees that are composed of a mix of voting and nonvoting members; and\n**(II)**\nartist representatives as members of the Board; and\n**(iii)**\nable to demonstrate to the Register that, by the date described under section 3(a)(2) the entity will have the administrative and technological capabilities to establish and administer the Fund in accordance with this Act; and\n**(B)**\nif no entity meets the criteria under subparagraph (A), an entity determined by the Register to most nearly fit such criteria.\n**(3) Eligible featured artist**\nThe term eligible featured artist means a featured artist who\u2014\n**(A)**\nregisters with the Fund; and\n**(B)**\nprovides the Fund Administrator with the information determined necessary by the Fund Administrator\u2014\n**(i)**\nidentify or locate such featured artist; and\n**(ii)**\nprovide payment to such featured artist (or a person designated by such artist to receive such payment on behalf of such artist).\n**(4) Eligible non-featured artist defined**\nIn this paragraph, the term eligible non-featured artist means a non-featured artist that provides the American Federation of Musicians and Screen Actors Guild and the American Federation of Television and Radio Artists Intellectual Property Rights Distribution Fund (or any successor Fund) with the information determined necessary by such Fund\u2014\n**(A)**\nto identify or locate such non-featured artist; and\n**(B)**\nprovide payment to the non-featured artist (or a person designated by such artist to receive such payment on behalf of such artist).\n**(5) End user**\nThe term end user means a unique person that receives an offering from the service provider, including the following:\n**(A)**\nA person who pays no fee for receiving the offering.\n**(B)**\nA person who pays a subscription fee for receiving the offering.\n**(6) Featured artist**\nThe term featured artist means an artist who is prominently featured on a sound recording made available through an offering.\n**(7) Fund**\nThe term Fund means the Artist Compensation Royalty Fund established by the Fund Administrator under section 2(a).\n**(8) Fund Administrator**\nThe term Fund Administrator means the eligible entity designated under section 2(a)(1).\n**(9) Living wage royalty fee**\nThe term living wage royalty fee means the additional free required to be charged under section 4(a).\n**(10) Master recording**\nThe term master recording means the original sound recording of a song.\n**(11) Non-featured artist**\nThe term non-featured artist \u2014\n**(A)**\nmeans an artist who is not prominently featured on a sound recording made available through an offering; and\n**(B)**\nincludes the following:\n**(i)**\nA session musician.\n**(ii)**\nA back-up vocalist.\n**(12) Non-subscription revenue**\nThe term non-subscription revenue means any revenue received from music streaming (including revenue received from advertising with respect to such music streaming), other than revenue from a subscription fee.\n**(13) Offering**\nThe term offering means the provision of a stream by a service provider.\n**(14) Qualifying stream**\nThe term qualifying stream means with respect to a master recording and a calendar month, the lesser of\u2014\n**(A)**\nthe number of streams of the master recording accrued by the eligible featured artist in that calendar month; and\n**(B)**\n1,000,000 streams.\n**(15) Register**\nThe term Register means the Register of Copyrights.\n**(16) Service provider**\nThe term service provider means an entity, that\u2014\n**(A)**\nprovides a stream to an end user;\n**(B)**\ncontracts with or has a direct relationship with an end user to provide such streams; and\n**(C)**\ncontrols which such streams are made available to such end users.\n**(17) Stream**\nThe term stream \u2014\n**(A)**\nmeans an interactive, encrypted digital transmission that embodies a master recording that allows a person to receive and listen to such master recording upon request at a time chosen by the person;\n**(B)**\ndoes not include a temporary copy of such master recording\u2014\n**(i)**\ngenerated by a service provider in the course of providing the transmission; and\n**(ii)**\nused solely for the purpose of caching or buffering.\n**(18) Subscription fee**\nThe term subscription fee means a monthly fee that a person pays to the service provider to access an offering of the service provider, whether or not the person pays the fee on a standalone basis or as part of a single transaction that includes such fee and another fee for one or more product or services having more than token value.",
      "versionDate": "2025-09-30",
      "versionType": "Introduced in House"
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
        "name": "Arts, Culture, Religion",
        "updateDate": "2025-12-08T17:53:12Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5664ih.xml"
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
      "title": "Living Wage for Musicians Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-21T11:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Living Wage for Musicians Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-21T11:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Artist Compensation Royalty Fund, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-21T11:18:11Z"
    }
  ]
}
```
