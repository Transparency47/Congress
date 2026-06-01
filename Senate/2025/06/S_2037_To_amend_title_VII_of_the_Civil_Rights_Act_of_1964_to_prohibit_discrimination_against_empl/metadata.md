# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2037?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2037
- Title: Restoring Biological Truth to the Workplace Act
- Congress: 119
- Bill type: S
- Bill number: 2037
- Origin chamber: Senate
- Introduced date: 2025-06-11
- Update date: 2025-12-05T22:56:31Z
- Update date including text: 2025-12-05T22:56:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-11: Introduced in Senate
- 2025-06-11 - IntroReferral: Introduced in Senate
- 2025-06-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-06-11: Introduced in Senate

## Actions

- 2025-06-11 - IntroReferral: Introduced in Senate
- 2025-06-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2037",
    "number": "2037",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Restoring Biological Truth to the Workplace Act",
    "type": "S",
    "updateDate": "2025-12-05T22:56:31Z",
    "updateDateIncludingText": "2025-12-05T22:56:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-11",
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

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-06-11T20:10:13Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "MO"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-07-08",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2037is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2037\nIN THE SENATE OF THE UNITED STATES\nJune 11, 2025 Mr. Banks introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend title VII of the Civil Rights Act of 1964 to prohibit discrimination against employees on the basis of expression that describes, asserts, or reinforces the binary or biological nature of sex.\n#### 1. Short title\nThis Act may be cited as the Restoring Biological Truth to the Workplace Act .\n#### 2. Prohibited unlawful employment action\nSection 703 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e\u20132 ) is amended by adding at the end the following:\n(o) (1) It shall be an unlawful employment practice for an employer to take an action described in subsection (a) because an employee engages in covered expression, that describes, asserts, or reinforces the binary or biological nature of sex. For purposes of this paragraph, the term covered expression means expression, inside or outside of a workplace, through means including speech, writing, or a depiction, or owning or using an item that contains speech, writing, or a depiction, and includes the use of pronouns. (2) It shall be an unlawful employment practice for an employer to take an action described in subsection (a) because an employee requests or uses a single-sex area that is a bathroom, changing area, or other area where physical privacy is desirable. (3) It shall not be a defense to the use of a practice described in paragraph (1) or (2) that use of the practice is job related for the position in question or consistent with business necessity. .\n#### 3. Prohibited retaliation\nSection 704(a) of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e\u20133(a) ) is amended by inserting , including an unlawful employment practice prohibited under section 703(o) after by this title .",
      "versionDate": "2025-06-11",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-07-21",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "4554",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Restoring Biological Truth to the Workplace Act",
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-07-02T13:11:41Z"
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
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2037is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Restoring Biological Truth to the Workplace Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-09T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Restoring Biological Truth to the Workplace Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-19T03:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title VII of the Civil Rights Act of 1964 to prohibit discrimination against employees on the basis of expression that describes, asserts, or reinforces the binary or biological nature of sex.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-19T03:33:19Z"
    }
  ]
}
```
