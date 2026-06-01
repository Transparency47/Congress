# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4680?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4680
- Title: Access to Homeownership Act
- Congress: 119
- Bill type: HR
- Bill number: 4680
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-03-27T08:06:45Z
- Update date including text: 2026-03-27T08:06:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4680",
    "number": "4680",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "J000310",
        "district": "32",
        "firstName": "Julie",
        "fullName": "Rep. Johnson, Julie [D-TX-32]",
        "lastName": "Johnson",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Access to Homeownership Act",
    "type": "HR",
    "updateDate": "2026-03-27T08:06:45Z",
    "updateDateIncludingText": "2026-03-27T08:06:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:05:25Z",
          "name": "Referred To"
        }
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
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "MI"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "IL"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "MD"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "OH"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "DE"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4680ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4680\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Ms. Johnson of Texas introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require multifamily borrowers with federally backed multifamily mortgage loans to submit positive rental payments to certain consumer reporting agencies.\n#### 1. Short title\nThis Act may be cited as the Access to Homeownership Act .\n#### 2. Positive rental payments\nThe Federal Housing Enterprises Financial Safety and Soundness Act of 1992 ( 12 U.S.C. 4541 et seq. ) is amended by inserting after section 1355 ( 12 U.S.C. 4602 ) the following:\n1355A. Positive rental payments (a) Definition In this section, the term federally backed multifamily mortgage loan includes any loan (other than temporary financing such as a construction loan) that\u2014 (1) is secured by a first or subordinate lien on residential multifamily real property designed principally for the occupancy of 5 or more families, including any such secured loan, the proceeds of which are used to prepay or pay off an existing loan secured by the same property; and (2) is made in whole or in part, or insured, guaranteed, supplemented, or assisted in any way, by any officer or agency of the Federal Government or under or in connection with a housing or urban development program administered by the Secretary of Housing and Urban Development or a housing or related program administered by any other such officer or agency, or is purchased or securitized by the Federal Home Loan Mortgage Corporation or the Federal National Mortgage Association. (b) Authority (1) In general The Director shall, by order or regulation, require each enterprise to establish and maintain a program requiring multifamily borrowers with federally backed multifamily mortgage loans to request the consent of their residents to report the positive rent payments of the residents directly to each consumer reporting agency described in section 603(p) of the Fair Credit Reporting Act ( 15 U.S.C. 1681a(p) ), including 24 months of prior positive rent payments (if available). (2) Requirements Multifamily borrowers with federally backed multifamily mortgage loans shall report positive rent payments described in paragraph (1) if the resident consents to such reporting. (c) Mortgages Any positive rent payment made by a resident described in subsection (b) shall be considered in an application to insure a mortgage under section 203 of the National Housing Act ( 12 U.S.C. 1709 ). (d) Administrative costs The administrative costs associated with reporting positive rental payments shall be covered by the enterprises. (e) Report The Director shall submit to Congress a report every 5 years on the programs established under this section. (f) Authorization of appropriations There are authorized to be appropriated such sums as may be necessary to carry out this section. .",
      "versionDate": "2025-07-23",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-09-17T16:48:04Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4680ih.xml"
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
      "title": "Access to Homeownership Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-07T10:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Access to Homeownership Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-07T10:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require multifamily borrowers with federally backed multifamily mortgage loans to submit positive rental payments to certain consumer reporting agencies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-07T10:03:21Z"
    }
  ]
}
```
