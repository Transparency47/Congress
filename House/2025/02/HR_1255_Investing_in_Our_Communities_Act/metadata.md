# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1255?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1255
- Title: Investing in Our Communities Act
- Congress: 119
- Bill type: HR
- Bill number: 1255
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2026-05-29T15:29:51Z
- Update date including text: 2026-05-29T15:29:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1255",
    "number": "1255",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000392",
        "district": "8",
        "firstName": "David",
        "fullName": "Rep. Kustoff, David [R-TN-8]",
        "lastName": "Kustoff",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Investing in Our Communities Act",
    "type": "HR",
    "updateDate": "2026-05-29T15:29:51Z",
    "updateDateIncludingText": "2026-05-29T15:29:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
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
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:06:00Z",
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
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "IN"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "WI"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "CA"
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
      "sponsorshipDate": "2025-09-02",
      "state": "PA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "FL"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1255ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1255\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Mr. Kustoff (for himself, Mr. Yakym , Ms. Moore of Wisconsin , and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to reinstate advance refunding bonds.\n#### 1. Short title\nThis Act may be cited as the Investing in Our Communities Act .\n#### 2. Treatment of advance refunding bonds\n##### (a) In general\nSection 149(d) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin paragraph (1), by striking to advance refund another bond and inserting as part of an issue described in paragraph (2), (3), or (4) ;\n**(2)**\nby redesignating paragraphs (2) and (3) as paragraphs (6) and (7), respectively; and\n**(3)**\nby inserting after paragraph (1) the following new paragraphs:\n(2) Certain private activity bonds An issue is described in this paragraph if any bond (issued as part of such issue) is issued to advance refund a private activity bond (other than a qualified 501(c)(3) bond). (3) Other bonds (A) In general An issue is described in this paragraph if any bond (issued as part of such issue), hereinafter in this paragraph referred to as the refunding bond , is issued to advance refund a bond unless\u2014 (i) the refunding bond is only\u2014 (I) the 1st advance refunding of the original bond if the original bond is issued after 1985, or (II) the 1st or 2nd advance refunding of the original bond if the original bond was issued before 1986, (ii) in the case of refunded bonds issued before 1986, the refunded bond is redeemed not later than the earliest date on which such bond may be redeemed at par or at a premium of 3 percent or less, (iii) in the case of refunded bonds issued after 1985, the refunded bond is redeemed not later than the earliest date on which such bond may be redeemed, (iv) the initial temporary period under section 148(c) ends\u2014 (I) with respect to the proceeds of the refunding bond not later than 30 days after the date of issue of such bond, and (II) with respect to the proceeds of the refunded bond on the date of issue of the refunding bond, and (v) in the case of refunded bonds to which section 148(e) did not apply, on and after the date of issue of the refunding bond, the amount of proceeds of the refunded bond invested in higher yielding investments (as defined in section 148(b)) which are nonpurpose investments (as defined in section 148(f)(6)(A)) does not exceed\u2014 (I) the amount so invested as part of a reasonably required reserve or replacement fund or during an allowable temporary period, and (II) the amount which is equal to the lesser of 5 percent of the proceeds of the issue of which the refunded bond is a part or $100,000 (to the extent such amount is allocable to the refunded bond). (B) Special rules for redemptions (i) Issuer must redeem only if debt service savings Clauses (ii) and (iii) of subparagraph (A) shall apply only if the issuer may realize present value debt service savings (determined without regard to administrative expenses) in connection with the issue of which the refunding bond is a part. (ii) Redemptions not required before 90th day For purposes of clauses (ii) and (iii) of subparagraph (A), the earliest date referred to in such clauses shall not be earlier than the 90th day after the date of issuance of the refunding bond. (4) Abusive transactions prohibited An issue is described in this paragraph if any bond (issued as part of such issue) is issued to advance refund another bond and a device is employed in connection with the issuance of such issue to obtain a material financial advantage (based on arbitrage) apart from savings attributable to lower interest rates. (5) Special rules for purposes of paragraph (3) For purposes of paragraph (3), bonds issued before the date of the enactment of this subsection shall be taken into account under subparagraph (A)(i) thereof except\u2014 (A) a refunding which occurred before 1986 shall be treated as an advance refunding only if the refunding bond was issued more than 180 days before the redemption of the refunded bond, and (B) a bond issued before 1986, shall be treated as advance refunded no more than once before March 15, 1986. .\n##### (b) Conforming amendment\nSection 148(f)(4)(C) of such Code is amended by redesignating clauses (xiv) through (xvi) as clauses (xv) through (xvii) and by inserting after clause (xiii) the following new clause:\n(xiv) Determination of initial temporary period For purposes of this subparagraph, the end of the initial temporary period shall be determined without regard to section 149(d)(3)(A)(iv). .\n##### (c) Effective date\nThe amendments made by this section shall apply to advance refunding bonds issued after the date of the enactment of this Act.",
      "versionDate": "2025-02-12",
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
        "actionDate": "2026-05-15",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "8864",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "LIFT Act",
      "type": "HR"
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
        "name": "Taxation",
        "updateDate": "2025-05-05T18:55:55Z"
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
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1255ih.xml"
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
      "title": "Investing in Our Communities Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T08:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Investing in Our Communities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T08:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to reinstate advance refunding bonds.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T08:18:31Z"
    }
  ]
}
```
