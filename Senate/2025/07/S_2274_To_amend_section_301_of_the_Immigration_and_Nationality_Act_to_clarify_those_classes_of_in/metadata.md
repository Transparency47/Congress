# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2274?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2274
- Title: Constitutional Citizenship Clarification Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2274
- Origin chamber: Senate
- Introduced date: 2025-07-15
- Update date: 2025-12-05T22:53:18Z
- Update date including text: 2025-12-05T22:53:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in Senate
- 2025-07-15 - IntroReferral: Introduced in Senate
- 2025-07-15 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-07-15: Introduced in Senate

## Actions

- 2025-07-15 - IntroReferral: Introduced in Senate
- 2025-07-15 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2274",
    "number": "2274",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Constitutional Citizenship Clarification Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:53:18Z",
    "updateDateIncludingText": "2025-12-05T22:53:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-15",
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
          "date": "2025-07-15T15:06:24Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "TN"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "OH"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2274is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2274\nIN THE SENATE OF THE UNITED STATES\nJuly 15, 2025 Mr. Cotton (for himself, Mr. Hagerty , Mr. Moreno , and Mr. Cramer ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend section 301 of the Immigration and Nationality Act to clarify those classes of individuals born in the United States who are not nationals or citizens of the United States at birth.\n#### 1. Short title\nThis Act may be cited as the Constitutional Citizenship Clarification Act of 2025 .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe right of birthright citizenship, established by section 1 of the 14th Amendment to the Constitution of the United States, is rooted in the common law doctrine of jus soli and limited by the principle that it is not the soil, but ligeantia and obedientia that make the subject born a citizen;\n**(2)**\nthe Supreme Court of the United States has long recognized that, under the principle of allegiance and obedience, the children of foreign diplomats or enemy troops born on United States soil are not entitled to birthright citizenship; and\n**(3)**\nunder that same principle, the children of foreign spies, saboteurs, terrorists, or other hostile actors, as well as the children of illegal aliens, should not be entitled to birthright citizenship.\n#### 3. Purpose\nThe purposes of this Act are\u2014\n**(1)**\nto codify the common law exception to birthright citizenship for ambassadors and invaders; and\n**(2)**\nto clarify that other categories of disloyal or disobedient aliens are also subject to such exception.\n#### 4. Citizenship at birth exclusions for certain persons born in the United States\nSection 301(a) of the Immigration and Nationality Act ( 8 U.S.C. 1401(a) ) is amended by striking the semicolon at the end and inserting the following: \u201c: Provided , That a person born in the United States shall not be considered subject to the jurisdiction of the United States if the person is born of alien parents who are\u2014\n**(1)**\nunlawfully present in the United States;\n**(2)**\npresent in the United States for diplomatic purposes; or\n**(3)**\nengaged in a hostile occupation of, or a hostile operation in, the United States;\u201d.",
      "versionDate": "2025-07-15",
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
        "actionDate": "2025-07-23",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "4741",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Constitutional Citizenship Clarification Act of 2025",
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
        "name": "Immigration",
        "updateDate": "2025-09-04T16:21:21Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2274is.xml"
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
      "title": "Constitutional Citizenship Clarification Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T02:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Constitutional Citizenship Clarification Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T02:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend section 301 of the Immigration and Nationality Act to clarify those classes of individuals born in the United States who are not nationals or citizens of the United States at birth.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T02:18:33Z"
    }
  ]
}
```
