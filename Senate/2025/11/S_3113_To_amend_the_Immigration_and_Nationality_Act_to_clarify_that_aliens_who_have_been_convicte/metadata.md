# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3113?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3113
- Title: Deporting Fraudsters Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3113
- Origin chamber: Senate
- Introduced date: 2025-11-05
- Update date: 2025-12-22T22:46:30Z
- Update date including text: 2025-12-22T22:46:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-05: Introduced in Senate
- 2025-11-05 - IntroReferral: Introduced in Senate
- 2025-11-05 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-11-05: Introduced in Senate

## Actions

- 2025-11-05 - IntroReferral: Introduced in Senate
- 2025-11-05 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-05",
    "latestAction": {
      "actionDate": "2025-11-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3113",
    "number": "3113",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Deporting Fraudsters Act of 2025",
    "type": "S",
    "updateDate": "2025-12-22T22:46:30Z",
    "updateDateIncludingText": "2025-12-22T22:46:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-05",
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
      "actionDate": "2025-11-05",
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
          "date": "2025-11-05T22:29:03Z",
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
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-11-05",
      "state": "TX"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-11-05",
      "state": "UT"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3113is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3113\nIN THE SENATE OF THE UNITED STATES\nNovember 5, 2025 Mr. Cruz (for himself, Mr. Cornyn , and Mr. Lee ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to clarify that aliens who have been convicted of defrauding the United States Government or unlawfully receiving public benefits are inadmissible and deportable.\n#### 1. Short title\nThis Act may be cited as the Deporting Fraudsters Act of 2025 .\n#### 2. Inadmissibility and deportability related to defrauding the United States Government or unlawfully receiving public benefits\n##### (a) Inadmissibility\nSection 212(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(2) ) is amended by adding at the end the following:\n(J) Defrauding the united states government or unlawfully receiving public benefits Any alien who has been convicted of, who admits having committed, or who admits committing acts constituting the essential elements of, an offense that involves defrauding the United States Government or unlawfully receiving a Federal public benefit (as such term is defined in section 401(c) of the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 ( 8 U.S.C. 1611(c) ) or a State or local public benefit (as such term is defined in section 411(c) of such Act ( 8 U.S.C. 1621(c) )), or a conspiracy to commit such an offense, is inadmissible. .\n##### (b) Deportability\nSection 237(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1227(a)(2) ) is amended by adding at the end the following:\n(G) Defrauding the united states government or unlawfully receiving public benefits Any alien who has been convicted of an offense that involves defrauding the United States Government or unlawfully receiving a Federal public benefit (as such term is defined in section 401(c) of the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 ( 8 U.S.C. 1611(c) ) or a State or local public benefit (as such term is defined in section 411(c) of such Act ( 8 U.S.C. 1621(c) )), or a conspiracy to commit such an offense, is deportable. .",
      "versionDate": "2025-11-05",
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
        "actionDate": "2025-03-06",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1958",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Deporting Fraudsters Act of 2025",
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
        "updateDate": "2025-11-19T15:29:02Z"
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
      "date": "2025-11-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3113is.xml"
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
      "title": "Deporting Fraudsters Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-05T12:03:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Deporting Fraudsters Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-08T05:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Immigration and Nationality Act to clarify that aliens who have been convicted of defrauding the United States Government or unlawfully receiving public benefits are inadmissible and deportable.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-08T05:18:16Z"
    }
  ]
}
```
