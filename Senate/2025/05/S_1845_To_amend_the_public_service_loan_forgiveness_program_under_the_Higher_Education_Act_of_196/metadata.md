# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1845?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1845
- Title: No Loan Forgiveness for Terrorists Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1845
- Origin chamber: Senate
- Introduced date: 2025-05-21
- Update date: 2025-12-05T22:54:45Z
- Update date including text: 2025-12-05T22:54:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-21: Introduced in Senate
- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-05-21: Introduced in Senate

## Actions

- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1845",
    "number": "1845",
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
    "title": "No Loan Forgiveness for Terrorists Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:54:45Z",
    "updateDateIncludingText": "2025-12-05T22:54:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-21",
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
      "actionDate": "2025-05-21",
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
          "date": "2025-05-21T20:33:17Z",
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
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "AL"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1845is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1845\nIN THE SENATE OF THE UNITED STATES\nMay 21, 2025 Mr. Banks (for himself and Mr. Tuberville ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the public service loan forgiveness program under the Higher Education Act of 1965 to ensure qualifying public service excludes employment with organizations that engage in activities that have a substantial illegal purpose.\n#### 1. Short title\nThis Act may be cited as the No Loan Forgiveness for Terrorists Act of 2025 .\n#### 2. Exclusion of organizations that engage in activities that have a substantial illegal purpose from public service loan forgiveness\nSection 455(m)(3) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(m)(3) ) is amended by adding at the end the following:\n(C) Exclusion from public service job Notwithstanding subparagraph (B), the term public service job excludes employment with any organization that engages in activities that have a substantial illegal purpose, including\u2014 (i) aiding or abetting a violation of section 275 of the Immigration and Nationality Act ( 8 U.S.C. 1325 ) or another Federal immigration law; (ii) materially supporting terrorism, including by facilitating funding to, or the operations of, cartels designated as Foreign Terrorist Organizations consistent with section 219 of the Immigration and Nationality Act ( 8 U.S.C. 1189 ), or by engaging in violence for the purpose of obstructing or influencing Federal Government policy; (iii) materially supporting child abuse, including the chemical or surgical castration or mutilation of children or the trafficking of children to transgender sanctuary States for purposes of emancipation from their lawful parents, in violation of applicable law; (iv) engaging in a pattern of aiding or abetting illegal discrimination; or (v) engaging in a pattern of violating State tort laws, including laws against trespassing, disorderly conduct, public nuisance, vandalism, or obstruction of highways. .",
      "versionDate": "2025-05-21",
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
        "actionDate": "2025-06-04",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "3739",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "No Loan Forgiveness for Terrorists Act of 2025",
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
        "updateDate": "2025-06-16T13:09:04Z"
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
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1845is.xml"
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
      "title": "No Loan Forgiveness for Terrorists Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-11T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Loan Forgiveness for Terrorists Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the public service loan forgiveness program under the Higher Education Act of 1965 to ensure qualifying public service excludes employment with organizations that engage in activities that have a substantial illegal purpose.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:37Z"
    }
  ]
}
```
