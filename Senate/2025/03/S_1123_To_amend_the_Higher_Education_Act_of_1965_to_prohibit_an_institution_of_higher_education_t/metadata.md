# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1123?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1123
- Title: College Employment Accountability Act
- Congress: 119
- Bill type: S
- Bill number: 1123
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2025-12-05T22:08:45Z
- Update date including text: 2025-12-05T22:08:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1123",
    "number": "1123",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
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
    "title": "College Employment Accountability Act",
    "type": "S",
    "updateDate": "2025-12-05T22:08:45Z",
    "updateDateIncludingText": "2025-12-05T22:08:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
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
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T20:28:48Z",
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
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "MO"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "AL"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "TX"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "AR"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "OH"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1123is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1123\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Mr. Banks (for himself and Mr. Hawley ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Higher Education Act of 1965 to prohibit an institution of higher education that employs unauthorized aliens from receiving funds from Federal student assistance or Federal institutional aid and to require institutions of higher education to participate in the E-Verify Program in order to be eligible to participate in any program authorized under title IV of such Act.\n#### 1. Short title\nThis Act may be cited as the College Employment Accountability Act .\n#### 2. Ineligibility due to employment of unauthorized aliens\nPart B of title I of the Higher Education Act of 1965 ( 20 U.S.C. 1011 et seq. ) is amended by adding at the end the following:\n124. Ineligibility due to employment of unauthorized aliens Notwithstanding any other provision of law, no institution of higher education shall be eligible to receive funds from Federal student assistance or Federal institutional aid under this Act if the institution is found to be in violation of section 274A of the Immigration and Nationality Act ( 8 U.S.C. 1324a ). .\n#### 3. Requirement to participate in the E-Verify Program\nSection 487(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1094(a) ) is amended by adding at the end the following:\n(30) The institution will participate in the E-Verify Program under section 403(a) of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1324a note). .\n#### 4. Department of Homeland Security monitoring and notification requirements\n##### (a) Monitoring\nThe Secretary of Homeland Security shall monitor every 6 months whether an institution of higher education is participating in the E-Verify Program under section 403(a) of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1324a note).\n##### (b) Notification\nThe Secretary of Homeland Security shall notify the Secretary of Education, not later than 10 days after the Secretary of Homeland Security finds\u2014\n**(1)**\nan institution of higher education to be in violation of section 274A of the Immigration and Nationality Act ( 8 U.S.C. 1324a ); or\n**(2)**\nthat an institution of higher education is not participating in the E-Verify Program under section 403(a) of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1324a note).",
      "versionDate": "2025-03-25",
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
        "actionDate": "2025-03-26",
        "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2367",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "College Employment Accountability Act",
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
        "name": "Education",
        "updateDate": "2025-04-10T13:17:51Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1123is.xml"
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
      "title": "College Employment Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-10T01:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "College Employment Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T01:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Higher Education Act of 1965 to prohibit an institution of higher education that employs unauthorized aliens from receiving funds from Federal student assistance or Federal institutional aid and to require institutions of higher education to participate in the E-Verify Program in order to be eligible to participate in any program authorized under title IV of such Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T01:48:25Z"
    }
  ]
}
```
