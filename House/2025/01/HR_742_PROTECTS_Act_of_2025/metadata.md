# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/742?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/742
- Title: PROTECTS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 742
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-12-18T09:06:56Z
- Update date including text: 2025-12-18T09:06:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/742",
    "number": "742",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001218",
        "district": "7",
        "firstName": "Richard",
        "fullName": "Rep. McCormick, Richard [R-GA-7]",
        "lastName": "McCormick",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "PROTECTS Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-18T09:06:56Z",
    "updateDateIncludingText": "2025-12-18T09:06:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:09:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "GA"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "FL"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "FL"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "GA"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "MD"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "WI"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "MS"
    },
    {
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "MT"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley [R-WV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "WV"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "SC"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "FL"
    },
    {
      "bioguideId": "A000375",
      "district": "19",
      "firstName": "Jodey",
      "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Arrington",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "WI"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TN"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "GA"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "AZ"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "IN"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "UT"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "MN"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John [R-VA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "VA"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "SD"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TN"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "AZ"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "CO"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "WI"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "NJ"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "NC"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "FL"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "TX"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-08-12",
      "state": "FL"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "SC"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr742ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 742\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. McCormick (for himself, Mr. Clyde , Mrs. Luna , Mr. Scott Franklin of Florida , Ms. Van Duyne , Mr. Fallon , Mr. Collins , Mr. Weber of Texas , Mr. Harris of Maryland , Mr. Grothman , Mr. Guest , Mr. Zinke , Mr. Babin , Mr. Moore of West Virginia , Mr. Ellzey , Mr. Norman , Mr. Webster of Florida , Mr. Arrington , Mr. Wied , Mr. Rose , Mr. Austin Scott of Georgia , Mr. Hamadeh of Arizona , Mr. Baird , Mr. Owens , Mr. Gooden , Mr. Jackson of Texas , Mr. Finstad , Mr. McGuire , Mr. Johnson of South Dakota , Mr. Ogles , and Mr. Gosar ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit Federal funds from being used to provide certain gender transition procedures to minors.\n#### 1. Short title\nThis Act may be cited as the Protecting Resources Of Taxpayers to Eliminate Childhood Transgender Surgeries Act of 2025 or the PROTECTS Act of 2025 .\n#### 2. Prohibiting Federal funds from being used to provide certain gender transition procedures to minors\n##### (a) In general\nNotwithstanding any other provision of law, no Federal funds may be used or otherwise made available to provide or refer for a specified gender transition procedure to an individual under the age of 18 or to reimburse any entity for providing such a procedure to such an individual.\n##### (b) Specified gender transition procedure defined\n**(1) In general**\nFor purposes of this paragraph, except as provided in paragraph (2), the term specified gender transition procedure means, with respect to an individual, any of the following when performed for the purpose of intentionally changing the body of such individual to no longer correspond to their sex:\n**(A)**\nPerforming any surgery, including\u2014\n**(i)**\ncastration;\n**(ii)**\norchiectomy;\n**(iii)**\nscrotoplasty;\n**(iv)**\nvasectomy;\n**(v)**\nhysterectomy;\n**(vi)**\noophorectomy;\n**(vii)**\novariectomy;\n**(viii)**\nmetoidioplasty;\n**(ix)**\npenectomy;\n**(x)**\nphalloplasty;\n**(xi)**\nvaginoplasty;\n**(xii)**\nvaginectomy;\n**(xiii)**\nvulvoplasty;\n**(xiv)**\nreduction thyrochondroplasty;\n**(xv)**\nchondrolaryngoplasty;\n**(xvi)**\nmastectomy; and\n**(xvii)**\nany plastic, cosmetic, or aesthetic surgery that feminizes or masculinizes the facial or other body features of an individual.\n**(B)**\nAny placement of chest implants to create feminine breasts.\n**(C)**\nAny placement of fat or artificial implants in the gluteal region.\n**(D)**\nAdministering, supplying, prescribing, dispensing, distributing, or otherwise conveying to an individual medications, including\u2014\n**(i)**\ngonadotropin-releasing hormone (GnRH) analogues or other puberty-blocking drugs to stop or delay normal puberty; and\n**(ii)**\ntestosterone, estrogen, or other androgens to an individual at doses that are supraphysiologic than would normally be produced endogenously in a healthy individual of the same age and sex.\n**(2) Exception**\nParagraph (1) shall not apply to the following when furnished to an individual by a health care provider with the consent of such individual\u2019s parent or legal guardian:\n**(A)**\nPuberty suppression or blocking prescription drugs for the purpose of normalizing puberty for an individual experiencing precocious puberty.\n**(B)**\nAppropriate and medically necessary procedures or treatments to correct for\u2014\n**(i)**\na medically verifiable genetic disorder of sex development, including\u2014\n**(I)**\n46,XX chromosomes with virilization;\n**(II)**\n46,XY chromosomes with undervirilization; and\n**(III)**\nboth ovarian and testicular tissue;\n**(ii)**\nsex chromosome structure, sex steroid hormone production, or sex hormone action, if determined to be abnormal by a physician through genetic or biochemical testing; or\n**(iii)**\ninfection, disease, injury, or disorder caused or exacerbated by a previous procedure described in paragraph (1), or a physical disorder, physical injury, or physical illness that would, as certified by a physician, place the individual in imminent danger of death or impairment of a major bodily function unless the procedure is performed, not including procedures performed for the alleviation of mental distress.\n**(3) Certain terms**\nFor purposes of this section:\n**(A) Sex**\nThe term sex , when referring to individual\u2019s sex, shall be understood to refer to either male or female, as biologically determined.\n**(B) Female**\nThe term female , when referring to a natural person, means an individual who naturally has, had, will have, or would have, but for a developmental or genetic anomaly or historical accident, the reproductive system that at some point produces, transports, and utilizes eggs for fertilization.\n**(C) Male**\nThe term male , when referring to a natural person, means an individual who naturally has, had, will have, or would have, but for a developmental or genetic anomaly or historical accident, the reproductive system that at some point produces, transports, and utilizes sperm for fertilization.",
      "versionDate": "2025-01-28",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Child health",
            "updateDate": "2025-03-27T14:53:11Z"
          },
          {
            "name": "Sex, gender, sexual orientation discrimination",
            "updateDate": "2025-03-27T14:53:08Z"
          },
          {
            "name": "Surgery and anesthesia",
            "updateDate": "2025-03-27T14:53:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-01T14:54:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr742",
          "measure-number": "742",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr742v00",
            "update-date": "2025-04-24"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting Resources Of Taxpayers to Eliminate Childhood Transgender Surgeries Act of 2025 or the PROTECTS Act of 2025</strong></p><p>This bill prohibits providing or using federal funds to perform, refer for, or reimburse any entity for certain\u00a0gender transition procedures for an individual under the age of 18.\u00a0</p><p>The bill\u2019s prohibition applies to certain gender transition procedures that are\u00a0performed to intentionally change an individual\u2019s body to no longer correspond to the individual's\u00a0biological\u00a0sex, including surgeries, medications, and implants specified in the bill. The bill provides exceptions for specified procedures, such as treating certain genetic abnormalities or preventing imminent death or impairment of a major bodily function, when performed by a health care provider with the consent of the individual\u2019s parent or legal guardian.\u00a0</p>"
        },
        "title": "PROTECTS Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr742.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Resources Of Taxpayers to Eliminate Childhood Transgender Surgeries Act of 2025 or the PROTECTS Act of 2025</strong></p><p>This bill prohibits providing or using federal funds to perform, refer for, or reimburse any entity for certain\u00a0gender transition procedures for an individual under the age of 18.\u00a0</p><p>The bill\u2019s prohibition applies to certain gender transition procedures that are\u00a0performed to intentionally change an individual\u2019s body to no longer correspond to the individual's\u00a0biological\u00a0sex, including surgeries, medications, and implants specified in the bill. The bill provides exceptions for specified procedures, such as treating certain genetic abnormalities or preventing imminent death or impairment of a major bodily function, when performed by a health care provider with the consent of the individual\u2019s parent or legal guardian.\u00a0</p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119hr742"
    },
    "title": "PROTECTS Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Resources Of Taxpayers to Eliminate Childhood Transgender Surgeries Act of 2025 or the PROTECTS Act of 2025</strong></p><p>This bill prohibits providing or using federal funds to perform, refer for, or reimburse any entity for certain\u00a0gender transition procedures for an individual under the age of 18.\u00a0</p><p>The bill\u2019s prohibition applies to certain gender transition procedures that are\u00a0performed to intentionally change an individual\u2019s body to no longer correspond to the individual's\u00a0biological\u00a0sex, including surgeries, medications, and implants specified in the bill. The bill provides exceptions for specified procedures, such as treating certain genetic abnormalities or preventing imminent death or impairment of a major bodily function, when performed by a health care provider with the consent of the individual\u2019s parent or legal guardian.\u00a0</p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119hr742"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr742ih.xml"
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
      "title": "PROTECTS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T11:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PROTECTS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T11:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Resources Of Taxpayers to Eliminate Childhood Transgender Surgeries Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T11:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit Federal funds from being used to provide certain gender transition procedures to minors.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T11:18:27Z"
    }
  ]
}
```
