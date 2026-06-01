# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3977?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3977
- Title: Bankruptcy Threshold Adjustment Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3977
- Origin chamber: Senate
- Introduced date: 2026-03-03
- Update date: 2026-03-24T19:55:51Z
- Update date including text: 2026-03-24T19:55:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in Senate
- 2026-03-03 - IntroReferral: Introduced in Senate
- 2026-03-03 - Calendars: Introduced in the Senate. Read the first time. Placed on Senate Legislative Calendar under Read the First Time.
- 2026-03-04 - Calendars: Read the second time. Placed on Senate Legislative Calendar under General Orders. Calendar No. 347.
- Latest action: 2026-03-03: Introduced in Senate

## Actions

- 2026-03-03 - IntroReferral: Introduced in Senate
- 2026-03-03 - Calendars: Introduced in the Senate. Read the first time. Placed on Senate Legislative Calendar under Read the First Time.
- 2026-03-04 - Calendars: Read the second time. Placed on Senate Legislative Calendar under General Orders. Calendar No. 347.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3977",
    "number": "3977",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Bankruptcy Threshold Adjustment Act of 2026",
    "type": "S",
    "updateDate": "2026-03-24T19:55:51Z",
    "updateDateIncludingText": "2026-03-24T19:55:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-04",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read the second time. Placed on Senate Legislative Calendar under General Orders. Calendar No. 347.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-03-03",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Introduced in the Senate. Read the first time. Placed on Senate Legislative Calendar under Read the First Time.",
      "type": "Calendars"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "IL"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "TX"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "RI"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "SC"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3977pcs.xml",
      "text": "II\nCalendar No. 347\n119th CONGRESS\n2d Session\nS. 3977\nIN THE SENATE OF THE UNITED STATES\nMarch 3, 2026 Mr. Grassley (for himself, Mr. Durbin , Mr. Cornyn , Mr. Whitehouse , Mr. Graham , and Mr. Coons ) introduced the following bill; which was read the first time\nMarch 4, 2026 Read the second time and placed on the calendar\nA BILL\nTo amend title 11, United States Code, to modify certain bankruptcy eligibility requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bankruptcy Threshold Adjustment Act of 2026 .\n#### 2. Debt limit modifications\n##### (a) Modification to the small business bankruptcy debt limit\nSection 1182(1) of title 11, United States Code, is amended to read as follows:\n(1) Debtor The term debtor \u2014 (A) subject to subparagraph (B), means a person engaged in commercial or business activities (including any affiliate of such person that is also a debtor under this title and excluding a person whose primary activity is the business of owning single asset real estate) that has aggregate noncontingent liquidated secured and unsecured debts as of the date of the filing of the petition or the date of the order for relief in an amount not more than $7,500,000 (excluding debts owed to 1 or more affiliates or insiders) not less than 50 percent of which arose from the commercial or business activities of the debtor; and (B) does not include\u2014 (i) any member of a group of affiliated debtors under this title that has aggregate noncontingent liquidated secured and unsecured debts in an amount greater than $7,500,000 (excluding debt owed to 1 or more affiliates or insiders); (ii) any debtor that is a corporation subject to the reporting requirements under section 13 or 15(d) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78m , 78o(d)); or (iii) any debtor that is an affiliate of a corporation described in clause (ii). .\n##### (b) Modification to the consumer bankruptcy debt limit\nSection 109 of title 11, United States Code is amended by striking subsection (e) and inserting the following:\n(e) Only an individual with regular income that owes, on the date of the filing of the petition, noncontingent, liquidated debts that aggregate less than $2,750,000 or an individual with regular income and such individual\u2019s spouse, except a stockbroker or a commodity broker, that owe, on the date of the filing of the petition, noncontingent, liquidated debts that aggregate less than $2,750,000 may be a debtor under chapter 13 of this title. .\n#### 3. Effective date\nThe amendments made by this Act shall apply to any case that is commenced under title 11, United States Code, on or after the date of enactment of this Act.",
      "versionDate": "2026-03-04",
      "versionType": "Placed on Calendar Senate"
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
        "actionDate": "2026-02-26",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "7730",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Bankruptcy Threshold Adjustment Act of 2026",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-03-09T14:14:10Z"
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
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3977pcs.xml"
        }
      ],
      "type": "Placed on Calendar Senate"
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
      "updateDate": "2026-03-06T03:53:22Z"
    },
    {
      "billTextVersionCode": "PCS",
      "billTextVersionName": "Placed on Calendar Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Bankruptcy Threshold Adjustment Act of 2026",
      "titleType": "Short Title(s) from PCS (Placed on Senate Calendar) bill text",
      "titleTypeCode": "152",
      "updateDate": "2026-03-06T03:53:21Z"
    },
    {
      "title": "A bill to amend title 11, United States Code, to modify certain bankruptcy eligibility requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-04T12:35:18Z"
    }
  ]
}
```
