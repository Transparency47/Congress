# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1631?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1631
- Title: Safe Access to Cash Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1631
- Origin chamber: House
- Introduced date: 2025-02-26
- Update date: 2026-04-22T08:06:52Z
- Update date including text: 2026-04-22T08:06:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-26: Introduced in House

## Actions

- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1631",
    "number": "1631",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "R000612",
        "district": "6",
        "firstName": "John",
        "fullName": "Rep. Rose, John W. [R-TN-6]",
        "lastName": "Rose",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Safe Access to Cash Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-22T08:06:52Z",
    "updateDateIncludingText": "2026-04-22T08:06:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-26",
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
      "actionDate": "2025-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T15:05:40Z",
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
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MD"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "WI"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "PA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "TN"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "TN"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "FL"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "NC"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "CA"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1631ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1631\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2025 Mr. Rose (for himself, Mr. Ivey , Mr. Fitzgerald , Mr. Meuser , Ms. Brownley , Mr. Foster , Mr. Ogles , and Mr. Kustoff ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to clarify that ATMs are in the care, custody, control, management, or possession of, any bank, credit union, or any savings and loan association regardless of whether the ATM is located on the physical premises of such an institution.\n#### 1. Short title\nThis Act may be cited as the Safe Access to Cash Act of 2025 .\n#### 2. ATM Robbery\nSection 2113 of title 18, United States Code, is amended by adding at the end the following:\n(i) The term ATM means any network-connected automated teller machine terminal that is connected to one or more of the global, national, or regional electronic financial networks that allow a depositor of any bank, credit union, or savings and loan association, by use at such ATM of a card or other access device, as defined in subsection (e)(1) of section 1029 of this title, issued or authorized by such depository institution, to access such depositor\u2019s account for the purpose of making withdrawals from or deposits to such account, or making inquiry as to the balance in such account, and includes any ATM owned, operated, or sponsored by a bank, credit union, or any savings and loan association. (j) For purposes of this section, an ATM, and any cash that is in transit to or being loaded into or unloaded from an ATM, shall be considered in the care, custody, control, management, or possession of, any bank, credit union, or any savings and loan association, regardless of whether\u2014 (1) the ATM is located on the physical premises of such an institution; or (2) the ATM is owned or operated by such an institution. .",
      "versionDate": "2025-02-26",
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
            "name": "Banking and financial institutions regulation",
            "updateDate": "2025-07-24T14:42:02Z"
          },
          {
            "name": "Crimes against property",
            "updateDate": "2025-07-24T14:42:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-18T16:30:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
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
          "measure-id": "id119hr1631",
          "measure-number": "1631",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-26",
          "originChamber": "HOUSE",
          "update-date": "2026-02-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1631v00",
            "update-date": "2026-02-12"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Safe Access to Cash Act of 2025</strong></p><p>This bill specifies that robbery offenses involving ATMs and related cash constitute crimes under the federal bank robbery statute.</p><p>Currently, the federal bank robbery statute makes it a federal crime to take or attempt to take, by force and violence or by intimidation, money or other property belonging to or in the care, custody, control, management, or possession of any bank, credit union, or savings and loan association.</p><p>However, federal circuit courts have split on whether forcing someone to withdraw money from an ATM constitutes an offense under the federal bank robbery statute. The\u00a0Fifth Circuit Court of Appeals has held that directly forcing a bank customer to withdraw money from an ATM does not constitute a federal bank robbery because the funds were in the possession of the customer, not the bank. In contrast, the\u00a0Tenth and\u00a0Seventh\u00a0Circuits have held that directly forcing a bank customer to withdraw money from an ATM constitutes a federal bank robbery because the funds belonged to the bank when the withdrawal occurred.</p><p>This bill specifies that for purposes of the federal bank robbery statute, an ATM and any cash in transit to, being loaded into, or being unloaded from an ATM is in the care, custody, control, management, or possession of, any bank, credit union, or any savings and loan association, regardless of whether the ATM is located on the physical premises of such an institution or owned or operated by such an institution.</p>"
        },
        "title": "Safe Access to Cash Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1631.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Safe Access to Cash Act of 2025</strong></p><p>This bill specifies that robbery offenses involving ATMs and related cash constitute crimes under the federal bank robbery statute.</p><p>Currently, the federal bank robbery statute makes it a federal crime to take or attempt to take, by force and violence or by intimidation, money or other property belonging to or in the care, custody, control, management, or possession of any bank, credit union, or savings and loan association.</p><p>However, federal circuit courts have split on whether forcing someone to withdraw money from an ATM constitutes an offense under the federal bank robbery statute. The\u00a0Fifth Circuit Court of Appeals has held that directly forcing a bank customer to withdraw money from an ATM does not constitute a federal bank robbery because the funds were in the possession of the customer, not the bank. In contrast, the\u00a0Tenth and\u00a0Seventh\u00a0Circuits have held that directly forcing a bank customer to withdraw money from an ATM constitutes a federal bank robbery because the funds belonged to the bank when the withdrawal occurred.</p><p>This bill specifies that for purposes of the federal bank robbery statute, an ATM and any cash in transit to, being loaded into, or being unloaded from an ATM is in the care, custody, control, management, or possession of, any bank, credit union, or any savings and loan association, regardless of whether the ATM is located on the physical premises of such an institution or owned or operated by such an institution.</p>",
      "updateDate": "2026-02-12",
      "versionCode": "id119hr1631"
    },
    "title": "Safe Access to Cash Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Safe Access to Cash Act of 2025</strong></p><p>This bill specifies that robbery offenses involving ATMs and related cash constitute crimes under the federal bank robbery statute.</p><p>Currently, the federal bank robbery statute makes it a federal crime to take or attempt to take, by force and violence or by intimidation, money or other property belonging to or in the care, custody, control, management, or possession of any bank, credit union, or savings and loan association.</p><p>However, federal circuit courts have split on whether forcing someone to withdraw money from an ATM constitutes an offense under the federal bank robbery statute. The\u00a0Fifth Circuit Court of Appeals has held that directly forcing a bank customer to withdraw money from an ATM does not constitute a federal bank robbery because the funds were in the possession of the customer, not the bank. In contrast, the\u00a0Tenth and\u00a0Seventh\u00a0Circuits have held that directly forcing a bank customer to withdraw money from an ATM constitutes a federal bank robbery because the funds belonged to the bank when the withdrawal occurred.</p><p>This bill specifies that for purposes of the federal bank robbery statute, an ATM and any cash in transit to, being loaded into, or being unloaded from an ATM is in the care, custody, control, management, or possession of, any bank, credit union, or any savings and loan association, regardless of whether the ATM is located on the physical premises of such an institution or owned or operated by such an institution.</p>",
      "updateDate": "2026-02-12",
      "versionCode": "id119hr1631"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1631ih.xml"
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
      "title": "Safe Access to Cash Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-18T04:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safe Access to Cash Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-18T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to clarify that ATMs are in the care, custody, control, management, or possession of, any bank, credit union, or any savings and loan association regardless of whether the ATM is located on the physical premises of such an institution.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-18T04:33:32Z"
    }
  ]
}
```
