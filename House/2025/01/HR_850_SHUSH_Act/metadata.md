# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/850?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/850
- Title: SHUSH Act
- Congress: 119
- Bill type: HR
- Bill number: 850
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2026-05-20T08:08:25Z
- Update date including text: 2026-05-20T08:08:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-31 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-31 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/850",
    "number": "850",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001115",
        "district": "27",
        "firstName": "Michael",
        "fullName": "Rep. Cloud, Michael [R-TX-27]",
        "lastName": "Cloud",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "SHUSH Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:25Z",
    "updateDateIncludingText": "2026-05-20T08:08:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:06:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-31T15:06:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TN"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "LA"
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
      "sponsorshipDate": "2025-01-31",
      "state": "AZ"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "MD"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "CO"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "IL"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "AZ"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "TN"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "WY"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "GA"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "MN"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "False",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "TX"
    },
    {
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "UT"
    },
    {
      "bioguideId": "F000485",
      "district": "14",
      "firstName": "Clay",
      "fullName": "Rep. Fuller, Clay [R-GA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Fuller",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "GA"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "TX"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2026-05-15",
      "state": "UT"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr850ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 850\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Cloud (for himself, Mr. Ogles , Mr. Higgins of Louisiana , Mr. Gosar , Mr. Harris of Maryland , Ms. Boebert , and Mrs. Miller of Illinois ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide that silencers be treated the same as firearms accessories.\n#### 1. Short title\nThis Act may be cited as the Silencers Help Us Save Hearing Act or the SHUSH Act .\n#### 2. Equal treatment of silencers and firearms\n##### (a) In general\nSection 5845(a) of the Internal Revenue Code of 1986 is amended by striking (7) any silencer and all that follows through ; and (8) and inserting ; and (7) .\n##### (b) Effective date\n**(1) In general**\nExcept as otherwise provided in this subsection, the amendment made by this section shall take effect on the date of the enactment of this Act.\n**(2) Transfers**\nIn the case of the tax imposed by section 5811 of such Code, the amendment made by this section shall apply with respect to transfers after October 22, 2015.\n#### 3. Treatment of certain silencers\nSection 5841 of the Internal Revenue Code of 1986 is amended by adding at the end the following:\n(f) Firearm silencers A person acquiring or possessing a firearm silencer in accordance with Chapter 44 of title 18, United States Code, shall be treated as meeting any registration and licensing requirements of the National Firearms Act (as in effect on the day before the date of the enactment of this subsection) with respect to such silencer. .\n#### 4. Preemption of certain State laws in relation to firearm silencers\nSection 927 of title 18, United States Code, is amended by adding at the end the following: Notwithstanding the preceding sentence, a law of a State or a political subdivision of a State that, as a condition of lawfully making, transferring, using, possessing, or transporting a firearm silencer in or affecting interstate or foreign commerce, imposes a tax on any such conduct, or a marking, recordkeeping or registration requirement with respect to the firearm silencer, shall have no force or effect. .\n#### 5. Silencers and mufflers not to be Federally regulated\n##### (a) Definitions\nSection 921(a) of title 18, United States Code, is amended\u2014\n**(1)**\nin paragraph (3), by striking (C) any firearm muffler or firearm silencer; or (D) and inserting or (C) ; and\n**(2)**\nby striking paragraph (24).\n##### (b) Penalties\nSection 924 of such title is amended\u2014\n**(1)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)(B)(ii) by striking , or is equipped with a firearm silencer or firearm muffler ; and\n**(B)**\nin paragraph (1)(C)(ii), by striking or is equipped with a firearm silencer or firearm muffler, ; and\n**(2)**\nin subsection (o), by striking or is equipped with a firearm silencer or muffler, .\n##### (c) Carrying of concealed firearms by qualified law enforcement officers\nSection 926B(e)(3) of such title is amended\u2014\n**(1)**\nin subparagraph (A), by adding and at the end;\n**(2)**\nby striking subparagraph (B); and\n**(3)**\nby redesignating subparagraph (C) as subparagraph (B).\n##### (d) Carrying of concealed firearms by qualified retired law enforcement officers\nSection 926C(e)(1)(C) of such title is amended\u2014\n**(1)**\nin clause (i), by adding and at the end; and\n**(2)**\nby striking clause (ii).",
      "versionDate": "2025-01-31",
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
        "actionDate": "2025-01-30",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "345",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SHUSH Act",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-04-04T20:14:04Z"
          },
          {
            "name": "Consumer Product Safety Commission",
            "updateDate": "2025-04-04T20:14:04Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2025-04-04T20:14:04Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-04-04T20:14:04Z"
          },
          {
            "name": "Federal preemption",
            "updateDate": "2025-04-04T20:14:04Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-04-04T20:14:04Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-04-04T20:14:04Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-04-04T20:14:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-04T13:47:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
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
          "measure-id": "id119hr850",
          "measure-number": "850",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-06-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr850v00",
            "update-date": "2025-06-16"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Silencers Help Us Save Hearing Act or the SHUSH Act</strong></p><p>This bill removes silencers from regulation under certain\u00a0federal statutes governing the sale, transfer, and possession of firearms.</p><p>Specifically, it removes silencers from the list of firearms subject to regulation (i.e., registration and licensing requirements) under the National Firearms Act (NFA). Additionally, it excludes a muffler or silencer from the list of firearms subject to regulation (e.g., background check requirements) under the Gun Control Act of 1968 (GCA).</p><p>Finally, the bill does the following:</p><ul><li>preempts state or local laws that tax or regulate firearm silencers,</li><li>specifies that a person who lawfully acquires or possesses a silencer under provisions of the GCA meets the registration and licensing requirements of the NFA,</li><li>eliminates mandatory minimum prison terms for a crime of violence or drug trafficking offense in which a defendant uses or carries a firearm equipped with a silencer or muffler, and</li><li>permits active and retired law enforcement officers to carry a concealed silencer.</li></ul>"
        },
        "title": "SHUSH Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr850.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Silencers Help Us Save Hearing Act or the SHUSH Act</strong></p><p>This bill removes silencers from regulation under certain\u00a0federal statutes governing the sale, transfer, and possession of firearms.</p><p>Specifically, it removes silencers from the list of firearms subject to regulation (i.e., registration and licensing requirements) under the National Firearms Act (NFA). Additionally, it excludes a muffler or silencer from the list of firearms subject to regulation (e.g., background check requirements) under the Gun Control Act of 1968 (GCA).</p><p>Finally, the bill does the following:</p><ul><li>preempts state or local laws that tax or regulate firearm silencers,</li><li>specifies that a person who lawfully acquires or possesses a silencer under provisions of the GCA meets the registration and licensing requirements of the NFA,</li><li>eliminates mandatory minimum prison terms for a crime of violence or drug trafficking offense in which a defendant uses or carries a firearm equipped with a silencer or muffler, and</li><li>permits active and retired law enforcement officers to carry a concealed silencer.</li></ul>",
      "updateDate": "2025-06-16",
      "versionCode": "id119hr850"
    },
    "title": "SHUSH Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Silencers Help Us Save Hearing Act or the SHUSH Act</strong></p><p>This bill removes silencers from regulation under certain\u00a0federal statutes governing the sale, transfer, and possession of firearms.</p><p>Specifically, it removes silencers from the list of firearms subject to regulation (i.e., registration and licensing requirements) under the National Firearms Act (NFA). Additionally, it excludes a muffler or silencer from the list of firearms subject to regulation (e.g., background check requirements) under the Gun Control Act of 1968 (GCA).</p><p>Finally, the bill does the following:</p><ul><li>preempts state or local laws that tax or regulate firearm silencers,</li><li>specifies that a person who lawfully acquires or possesses a silencer under provisions of the GCA meets the registration and licensing requirements of the NFA,</li><li>eliminates mandatory minimum prison terms for a crime of violence or drug trafficking offense in which a defendant uses or carries a firearm equipped with a silencer or muffler, and</li><li>permits active and retired law enforcement officers to carry a concealed silencer.</li></ul>",
      "updateDate": "2025-06-16",
      "versionCode": "id119hr850"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr850ih.xml"
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
      "title": "SHUSH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-28T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SHUSH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Silencers Help Us Save Hearing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide that silencers be treated the same as firearms accessories.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T05:18:35Z"
    }
  ]
}
```
