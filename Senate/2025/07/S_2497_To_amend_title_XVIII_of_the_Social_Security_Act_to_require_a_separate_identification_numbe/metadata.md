# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2497?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2497
- Title: Fair Billing Act
- Congress: 119
- Bill type: S
- Bill number: 2497
- Origin chamber: Senate
- Introduced date: 2025-07-29
- Update date: 2026-02-05T17:34:30Z
- Update date including text: 2026-02-05T17:34:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in Senate
- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-07-29: Introduced in Senate

## Actions

- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2497",
    "number": "2497",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001076",
        "district": "",
        "firstName": "Maggie",
        "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
        "lastName": "Hassan",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Fair Billing Act",
    "type": "S",
    "updateDate": "2026-02-05T17:34:30Z",
    "updateDateIncludingText": "2026-02-05T17:34:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T15:31:16Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2497is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2497\nIN THE SENATE OF THE UNITED STATES\nJuly 29, 2025 Ms. Hassan (for herself and Mr. Marshall ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to require a separate identification number and an attestation for each off-campus outpatient department of a provider.\n#### 1. Short title\nThis Act may be cited as the Fair Billing Act .\n#### 2. Requiring a separate identification number and an attestation for each off-campus outpatient department of a provider\n##### (a) In general\nSection 1833(t) of the Social Security Act ( 42 U.S.C. 1395l(t) ) is amended by adding at the end the following new paragraph:\n(23) Use of unique health identifiers; attestation (A) In general No payment may be made under this subsection (or under an applicable payment system pursuant to paragraph (21)) for items and services furnished on or after January 1, 2026, by an off-campus outpatient department of a provider (as defined in subparagraph (C)) unless\u2014 (i) such department has obtained, and such items and services are billed under, a standard unique health identifier for health care providers (as described in section 1173(b)) that is separate from such identifier for such provider; (ii) such provider has submitted to the Secretary, during the 2-year period ending on the date such items and services are so furnished, an initial provider-based status attestation that such department is compliant with the requirements described in section 413.65 of title 42, Code of Federal Regulations (or a successor regulation); and (iii) after such provider has submitted an attestation under clause (ii), such provider has submitted a subsequent attestation within the timeframe specified by the Secretary. (B) Process for submission and review Not later than 1 year after the date of enactment of this paragraph, the Secretary shall, through notice and comment rulemaking, establish a process for each provider with an off-campus outpatient department of a provider to submit an initial and subsequent attestation pursuant to clauses (ii) and (iii), respectively, of subparagraph (A), and for the Secretary to review each such attestation and determine, through site visits, remote audits, or other means (as determined appropriate by the Secretary), whether such department is compliant with the requirements described in such subparagraph. (C) Off-campus outpatient department of a provider defined For purposes of this paragraph, the term off-campus outpatient department of a provider means a department of a provider (as defined in section 413.65 of title 42, Code of Federal Regulations, or any successor regulation) that is not located\u2014 (i) on the campus (as defined in such section) of such provider; or (ii) within the distance (described in such definition of campus) from a remote location of a hospital facility (as defined in such section). .\n##### (b) HHS OIG analysis\nNot later than January 1, 2030, the Inspector General of the Department of Health and Human Services shall submit to Congress\u2014\n**(1)**\nan analysis of the process established by the Secretary of Health and Human Services to conduct the reviews and determinations described in section 1833(t)(23)(B) of the Social Security Act, as added by subsection (a) of this section; and\n**(2)**\nrecommendations based on such analysis, as the Inspector General determines appropriate.",
      "versionDate": "2025-07-29",
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
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Care Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-02-03",
        "text": "Became Public Law No: 119-75."
      },
      "number": "7148",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Consolidated Appropriations Act, 2026",
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
        "name": "Health",
        "updateDate": "2025-09-17T17:10:16Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2497is.xml"
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
      "title": "Fair Billing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T04:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fair Billing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to require a separate identification number and an attestation for each off-campus outpatient department of a provider.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:33:31Z"
    }
  ]
}
```
