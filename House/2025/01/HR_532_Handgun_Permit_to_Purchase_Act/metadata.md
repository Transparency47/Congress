# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/532?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/532
- Title: Handgun Permit to Purchase Act
- Congress: 119
- Bill type: HR
- Bill number: 532
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-12-05T21:54:06Z
- Update date including text: 2025-12-05T21:54:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/532",
    "number": "532",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "R000606",
        "district": "8",
        "firstName": "Jamie",
        "fullName": "Rep. Raskin, Jamie [D-MD-8]",
        "lastName": "Raskin",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Handgun Permit to Purchase Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:54:06Z",
    "updateDateIncludingText": "2025-12-05T21:54:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
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
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:09:15Z",
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
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr532ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 532\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Raskin (for himself and Mrs. Hayes ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo authorize for a grant program for handgun licensing programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Handgun Permit to Purchase Act .\n#### 2. Findings\nCongress finds as follows:\n**(1)**\nIn 2023, gun violence claimed 46,728 lives, marking the third-highest number of gun-related deaths ever recorded in the United States in a single year.\n**(2)**\nBetween 2018 and 2022, approximately 90 percent of the firearm violence committed in the United States for which a firearm type was specified involved a handgun.\n**(3)**\nDuring the 5-year period described in paragraph (2), 35,959 people in the United States were killed with a handgun.\n**(4)**\nResearch by top national experts shows that\u2014\n**(A)**\nthe adoption of handgun purchaser licensing laws is associated with significant reductions in firearm-related homicides; and\n**(B)**\nthe repeal of handgun purchaser licensing laws is associated with significant increases in firearm-related homicides.\n**(5)**\nResearch on the effects of the adoption of a handgun purchaser licensing law in Connecticut in 1995 showed\u2014\n**(A)**\na 27.8-percent reduction in the rate of firearm homicide; and\n**(B)**\na 32.8-percent reduction in firearm suicide rates.\n**(6)**\nPublished research has shown that the repeal of a handgun purchaser licensing law in Missouri in 2007 was associated with\u2014\n**(A)**\na 47.3-percent increase in the rate of firearm homicide; and\n**(B)**\na 23.5-percent increase in firearm suicide rates.\n**(7)**\nResearch on the impact of the adoption of a handgun purchaser licensing law in Maryland in 2013 found\u2014\n**(A)**\nthat the adoption was associated with an 82-percent reduction in the Baltimore Police Department\u2019s recovery of handguns with key indications of diversion for criminal use; and\n**(B)**\nthat 41-percent of prohibited purchasers surveyed in Baltimore reported greater difficulty in obtaining a handgun.\n**(8)**\nResearch on the effects of firearm purchaser licensing laws throughout 3 decades found that\u2014\n**(A)**\nin urban counties between 1984 and 2015, firearm purchaser licensing laws were associated with an 11 percent reduction in firearm homicides; and\n**(B)**\nbetween 1984 and 2017, States with strong firearm purchaser licensing laws were associated with 56 percent lower rates of fatal mass shooting incidents and 67 percent fewer mass shooting victims.\n**(9)**\nIn States that have had effective handgun purchaser licensing laws for decades, such as Connecticut, Massachusetts, New Jersey, and New York, the vast majority of firearms traced to crimes originated in States that do not have handgun purchaser licensing laws, which supports the need for handgun purchaser licensing laws in every State.\n**(10)**\nResearch has shown that States with handgun purchaser licensing laws export far fewer firearms for criminal use in other States than States that lack handgun purchaser licensing laws.\n**(11)**\nOn January 13, 2025, the Supreme Court of the United States declined to hear a challenge to Maryland\u2019s handgun licensing law, allowing the ruling of the United States Court of Appeals for the Fourth Circuit, which upheld the constitutionality of the law, to stand.\n#### 3. Grant program authorized for handgun licensing\n##### (a) In general\nTitle I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10101 et seq. ) is amended by adding at the end the following:\nPP HANDGUN LICENSING GRANT PROGRAM 3061. Definition In this part, the term handgun has the meaning given the term in section 921(a) of title 18, United States Code. 3062. Grant program (a) In general The Attorney General may award grants to States, units of local government, and Indian tribes for the development, implementation, and evaluation of handgun purchaser licensing requirements. (b) Program authorized From the amounts appropriated to carry out this part, and not later than 90 days after such amounts are appropriated, the Attorney General shall award grants, on a competitive basis, to eligible applicants whose applications are approved under subsection (c) to assist such applicants in implementing and improving handgun purchaser licensing programs. (c) Application To be eligible to receive a grant under this part, a State, unit of local government, or Indian tribe shall submit to the Attorney General an application at such time, in such manner, and containing such information as the Attorney General may require, including\u2014 (1) a description of the law that the applicant has enacted to require a license for any purchase of a handgun, including a description of any exemptions to such law; and (2) a description of how the applicant will use the grant to carry out or improve its handgun purchaser licensing program. (d) Eligibility requirements To be eligible for a grant under this part, an applicant shall have in effect a handgun purchaser licensing law that includes the following requirements: (1) With respect to an individual applying for a handgun license or permit\u2014 (A) the individual shall be\u2014 (i) not less than 21 years old; and (ii) a citizen or national of the United States or an alien lawfully admitted for permanent residence (as those terms are defined in section 101(a) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a) )); (B) the individual shall apply for the handgun purchaser license or permit at a law enforcement agency in the State in which the individual resides; (C) the individual shall reapply for the handgun purchaser license or permit after a period not longer than 5 years; and (D) the individual shall, in connection with the application for the handgun purchaser license or permit\u2014 (i) submit to a background investigation and a criminal history check, as established by the State, which shall ensure, at a minimum, that the individual is not prohibited from possessing a firearm under section 922(g) of title 18, United States Code; and (ii) submit fingerprints and photographs. (2) An individual who is prohibited from possessing a firearm under section 922(g) of title 18, United States Code, may not be issued a handgun purchasing license or permit. (e) Use of funds Grant funds awarded under this part shall be used to improve the handgun purchaser licensing program of the grant recipient. .\n##### (b) Authorization of appropriations\nSection 1001(a) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10261(a) ) is amended by adding at the end the following:\n(29) There are authorized to be appropriated such sums as may be necessary to carry out part PP. .",
      "versionDate": "2025-01-16",
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
        "actionDate": "2025-01-16",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "123",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Handgun Permit to Purchase Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Criminal justice information and records",
            "updateDate": "2025-02-19T21:27:07Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-02-19T21:27:07Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-02-19T21:27:07Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-02-19T21:27:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-02-15T16:09:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr532",
          "measure-number": "532",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr532v00",
            "update-date": "2025-04-24"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Handgun Permit to Purchase Act</b></p> <p>This bill authorizes a grant program for states, local governments, and Indian tribes to implement and evaluate handgun purchaser licensing requirements.</p>"
        },
        "title": "Handgun Permit to Purchase Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr532.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Handgun Permit to Purchase Act</b></p> <p>This bill authorizes a grant program for states, local governments, and Indian tribes to implement and evaluate handgun purchaser licensing requirements.</p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119hr532"
    },
    "title": "Handgun Permit to Purchase Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Handgun Permit to Purchase Act</b></p> <p>This bill authorizes a grant program for states, local governments, and Indian tribes to implement and evaluate handgun purchaser licensing requirements.</p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119hr532"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr532ih.xml"
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
      "title": "Handgun Permit to Purchase Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T11:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Handgun Permit to Purchase Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-14T11:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize for a grant program for handgun licensing programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-14T11:03:22Z"
    }
  ]
}
```
