# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7730?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7730
- Title: Bankruptcy Threshold Adjustment Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7730
- Origin chamber: House
- Introduced date: 2026-02-26
- Update date: 2026-03-31T15:48:32Z
- Update date including text: 2026-03-31T15:48:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-26: Introduced in House
- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported (Amended) by Voice Vote.
- Latest action: 2026-02-26: Introduced in House

## Actions

- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported (Amended) by Voice Vote.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-26",
    "latestAction": {
      "actionDate": "2026-02-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7730",
    "number": "7730",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "C001118",
        "district": "6",
        "firstName": "Ben",
        "fullName": "Rep. Cline, Ben [R-VA-6]",
        "lastName": "Cline",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Bankruptcy Threshold Adjustment Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-31T15:48:32Z",
    "updateDateIncludingText": "2026-03-31T15:48:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
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
      "actionDate": "2026-02-26",
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
      "actionDate": "2026-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-26",
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
            "date": "2026-03-26T18:27:43Z",
            "name": "Markup By"
          },
          {
            "date": "2026-02-26T14:30:15Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "CO"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "TX"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7730ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7730\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2026 Mr. Cline (for himself, Mr. Correa , Ms. Lee of Florida , and Mr. Neguse ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 11, United States Code, to modify certain bankruptcy eligibility requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bankruptcy Threshold Adjustment Act of 2026 .\n#### 2. Debt limit modifications\n##### (a) Modification to the small business bankruptcy debt limit\nSection 1182(1) of title 11, United States Code, is amended to read as follows:\n(1) Debtor The term debtor \u2014 (A) subject to subparagraph (B), means a person engaged in commercial or business activities (including any affiliate of such person that is also a debtor under this title and excluding a person whose primary activity is the business of owning single asset real estate) that has aggregate noncontingent liquidated secured and unsecured debts as of the date of the filing of the petition or the date of the order for relief in an amount not more than $7,500,000 (excluding debts owed to 1 or more affiliates or insiders) not less than 50 percent of which arose from the commercial or business activities of the debtor; and (B) does not include\u2014 (i) any member of a group of affiliated debtors under this title that has aggregate noncontingent liquidated secured and unsecured debts in an amount greater than $7,500,000 (excluding debt owed to 1 or more affiliates or insiders); (ii) any debtor that is a corporation subject to the reporting requirements under section 13 or 15(d) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78m , 78o(d)); or (iii) any debtor that is an affiliate of a corporation described in clause (ii). .\n##### (b) Modification to the consumer bankruptcy debt limit\nSection 109 of title 11, United States Code, is amended by striking subsection (e) and inserting the following:\n(e) Only an individual with regular income that owes, on the date of the filing of the petition, noncontingent, liquidated debts that aggregate less than $2,750,000 or an individual with regular income and such individual\u2019s spouse, except a stockbroker or a commodity broker, that owe, on the date of the filing of the petition, noncontingent, liquidated debts that aggregate less than $2,750,000 may be a debtor under chapter 13 of this title. .\n#### 3. Effective date\nThe amendments made by this Act shall apply to any case that is commenced under title 11, United States Code, on or after the date of enactment of this Act.",
      "versionDate": "2026-02-26",
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
        "actionDate": "2026-03-04",
        "text": "Read the second time. Placed on Senate Legislative Calendar under General Orders. Calendar No. 347."
      },
      "number": "3977",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Bankruptcy Threshold Adjustment Act of 2026",
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
            "name": "Bankruptcy",
            "updateDate": "2026-03-31T15:28:28Z"
          },
          {
            "name": "Debt collection",
            "updateDate": "2026-03-31T15:48:32Z"
          },
          {
            "name": "Small business",
            "updateDate": "2026-03-31T15:28:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2026-03-24T19:56:00Z"
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
      "date": "2026-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7730ih.xml"
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
      "title": "Bankruptcy Threshold Adjustment Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T02:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bankruptcy Threshold Adjustment Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T02:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 11, United States Code, to modify certain bankruptcy eligibility requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T02:03:20Z"
    }
  ]
}
```
