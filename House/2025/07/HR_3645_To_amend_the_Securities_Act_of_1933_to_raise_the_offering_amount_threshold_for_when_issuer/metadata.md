# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3645?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3645
- Title: ACCESS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3645
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2026-03-18T20:13:02Z
- Update date including text: 2026-03-18T20:13:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-06-10 - Committee: Committee Consideration and Mark-up Session Held
- 2025-06-10 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 51 - 0.
- 2025-07-15 - Calendars: Placed on the Union Calendar, Calendar No. 166.
- 2025-07-15 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-203.
- 2025-07-15 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-203.
- Latest action: 2025-05-29: Introduced in House

## Actions

- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-06-10 - Committee: Committee Consideration and Mark-up Session Held
- 2025-06-10 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 51 - 0.
- 2025-07-15 - Calendars: Placed on the Union Calendar, Calendar No. 166.
- 2025-07-15 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-203.
- 2025-07-15 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-203.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3645",
    "number": "3645",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001204",
        "district": "9",
        "firstName": "Daniel",
        "fullName": "Rep. Meuser, Daniel [R-PA-9]",
        "lastName": "Meuser",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "ACCESS Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-18T20:13:02Z",
    "updateDateIncludingText": "2026-03-18T20:13:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2025-07-15",
      "calendarNumber": {
        "calendar": "U00166"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 166.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2025-07-15",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-203.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2025-07-15",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-203.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-10",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 51 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-10",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-29",
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
        "item": [
          {
            "date": "2025-07-15T23:00:45Z",
            "name": "Reported By"
          },
          {
            "date": "2025-06-10T17:06:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-29T15:04:25Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "True",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "TX"
    },
    {
      "bioguideId": "M001136",
      "district": "9",
      "firstName": "Lisa",
      "fullName": "Rep. McClain, Lisa C. [R-MI-9]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "MI"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "IA"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3645ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3645\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Mr. Meuser (for himself, Ms. De La Cruz , Mrs. McClain , Mr. Nunn of Iowa , and Ms. Salazar ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Securities Act of 1933 to raise the offering amount threshold for when issuers using the crowdfunding exemption are required to file financial statements reviewed by a public accountant who is independent of the issuer, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Amendment for Crowdfunding Capital Enhancement and Small-business Support Act of 2025 or the ACCESS Act of 2025 .\n#### 2. Offering threshold for reviews by public accountant\n##### (a) In general\nSection 4A(b)(1)(D) of the Securities Act of 1933 ( 15 U.S.C. 77d\u20131(b)(1)(D) ) is amended by striking $100,000 each place such term appears and inserting $500,000 .\n##### (b) Technical correction\nSection 4A of the Securities Act of 1933 ( 15 U.S.C. 77d\u20131 ) is amended\u2014\n**(1)**\nby striking section 4(6) each place such term appears and inserting section 4(a)(6) ; and\n**(2)**\nby striking section 4(6)(B) each place such term appears and inserting section 4(a)(6)(B) .",
      "versionDate": "2025-05-29",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3645rh.xml",
      "text": "IB\nUnion Calendar No. 166\n119th CONGRESS\n1st Session\nH. R. 3645\n[Report No. 119\u2013203]\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Mr. Meuser (for himself, Ms. De La Cruz , Mrs. McClain , Mr. Nunn of Iowa , and Ms. Salazar ) introduced the following bill; which was referred to the Committee on Financial Services\nJuly 15, 2025 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on May 29, 2025\nA BILL\nTo amend the Securities Act of 1933 to raise the offering amount threshold for when issuers using the crowdfunding exemption are required to file financial statements reviewed by a public accountant who is independent of the issuer, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Amendment for Crowdfunding Capital Enhancement and Small-business Support Act of 2025 or the ACCESS Act of 2025 .\n#### 2. Offering threshold for reviews by public accountant\n##### (a) In general\nSection 4A of the Securities Act of 1933 ( 15 U.S.C. 77d\u20131 ) is amended\u2014\n**(1)**\nin subsection (b)(1)(D), by striking $100,000 each place such term appears and inserting $250,000 ; and\n**(2)**\nby adding at the end the following:\n(i) Discretion to adjust amount The Commission may increase the amount specified in subsections (b)(1)(D)(i) and (b)(1)(D)(ii) from $250,000 to an amount not greater than $400,000 upon the recommendation of the Office of the Advocate for Small Business Capital Formation and the Office of the Investor Advocate. .\n##### (b) Technical corrections\nSection 4A of the Securities Act of 1933 ( 15 U.S.C. 77d\u20131 ) is amended\u2014\n**(1)**\nby striking section 4(6) each place such term appears and inserting section 4(a)(6) ; and\n**(2)**\nby striking section 4(6)(B) each place such term appears and inserting section 4(a)(6)(B) .",
      "versionDate": "2025-07-15",
      "versionType": "Reported in House"
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
        "actionDate": "2026-01-15",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "3662",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ACCESS Act of 2026",
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
            "name": "Business records",
            "updateDate": "2025-06-30T14:10:30Z"
          },
          {
            "name": "Corporate finance and management",
            "updateDate": "2025-06-30T14:10:22Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2025-06-30T14:07:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-06-12T14:11:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-15",
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
          "measure-id": "id119hr3645",
          "measure-number": "3645",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-15",
          "originChamber": "HOUSE",
          "update-date": "2025-09-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3645v07",
            "update-date": "2025-09-03"
          },
          "action-date": "2025-07-15",
          "action-desc": "Reported to House",
          "summary-text": "<p><strong>Amendment for Crowdfunding Capital Enhancement and Small-business Support Act of 2025 or the ACCESS Act of 2025 </strong></p><p>This bill expands the exemption from certain disclosures applicable to crowdfunding issuers with specified target offering amounts. (Crowdfunding is used to raise capital through a large number of individuals investing potentially small amounts of money.) Under current law, crowdfunding issuers that have target offering amounts of $100,000 or less are not required to make available financial statements reviewed by an independent public accountant. The bill increases that amount to $250,000 and allows the Securities and Exchange Commission to increase this amount to no more than $400,000 upon recommendation of the Office of the Advocate for Small Business Capital Formation and the Office of the Investor Advocate.</p>"
        },
        "title": "ACCESS Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3645.xml",
    "summary": {
      "actionDate": "2025-07-15",
      "actionDesc": "Reported to House",
      "text": "<p><strong>Amendment for Crowdfunding Capital Enhancement and Small-business Support Act of 2025 or the ACCESS Act of 2025 </strong></p><p>This bill expands the exemption from certain disclosures applicable to crowdfunding issuers with specified target offering amounts. (Crowdfunding is used to raise capital through a large number of individuals investing potentially small amounts of money.) Under current law, crowdfunding issuers that have target offering amounts of $100,000 or less are not required to make available financial statements reviewed by an independent public accountant. The bill increases that amount to $250,000 and allows the Securities and Exchange Commission to increase this amount to no more than $400,000 upon recommendation of the Office of the Advocate for Small Business Capital Formation and the Office of the Investor Advocate.</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119hr3645"
    },
    "title": "ACCESS Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-07-15",
      "actionDesc": "Reported to House",
      "text": "<p><strong>Amendment for Crowdfunding Capital Enhancement and Small-business Support Act of 2025 or the ACCESS Act of 2025 </strong></p><p>This bill expands the exemption from certain disclosures applicable to crowdfunding issuers with specified target offering amounts. (Crowdfunding is used to raise capital through a large number of individuals investing potentially small amounts of money.) Under current law, crowdfunding issuers that have target offering amounts of $100,000 or less are not required to make available financial statements reviewed by an independent public accountant. The bill increases that amount to $250,000 and allows the Securities and Exchange Commission to increase this amount to no more than $400,000 upon recommendation of the Office of the Advocate for Small Business Capital Formation and the Office of the Investor Advocate.</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119hr3645"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3645ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3645rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "ACCESS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:57Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Securities Act of 1933 to raise the offering amount threshold for when issuers using the crowdfunding exemption are required to file financial statements reviewed by a public accountant who is independent of the issuer, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-17T11:31:57Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "ACCESS Act of 2025",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-07-16T04:23:22Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Amendment for Crowdfunding Capital Enhancement and Small-business Support Act of 2025",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-07-16T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ACCESS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Amendment for Crowdfunding Capital Enhancement and Small-business Support Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:20Z"
    }
  ]
}
```
