# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3318?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3318
- Title: American Citizens First Act
- Congress: 119
- Bill type: S
- Bill number: 3318
- Origin chamber: Senate
- Introduced date: 2025-12-03
- Update date: 2026-01-07T17:35:29Z
- Update date including text: 2026-01-07T17:35:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in Senate
- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-12-03: Introduced in Senate

## Actions

- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3318",
    "number": "3318",
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
    "title": "American Citizens First Act",
    "type": "S",
    "updateDate": "2026-01-07T17:35:29Z",
    "updateDateIncludingText": "2026-01-07T17:35:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-03",
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
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T16:19:04Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3318is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3318\nIN THE SENATE OF THE UNITED STATES\nDecember 3, 2025 Mr. Cotton introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo terminate Federal benefits for noncitizens, to authorize the denaturalization of naturalized citizens who undermine domestic tranquility, to expand expedited removal authority, to require mandatory revetting of nationals of Afghanistan, and to provide for automatic termination of temporary protected status, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Citizens First Act .\n#### 2. Termination of Federal benefits for noncitizens\nNotwithstanding any other provision of law, no person who is not a citizen or national of the United States shall be eligible for any Federal public benefit (as defined in section 401(c) of the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 ( 8 U.S.C. 1611(c) )), including\u2014\n**(1)**\nany form of welfare or needs-based cash assistance;\n**(2)**\nMedicaid (except emergency medical services);\n**(3)**\nthe Supplemental Nutrition Assistance Program or food stamps;\n**(4)**\nFederal housing assistance;\n**(5)**\nFederal student financial aid; and\n**(6)**\nthe refundable portion of any tax credit under the Internal Revenue Code of 1986.\n#### 3. Denaturalization for acts undermining domestic tranquility\nSection 340 of the Immigration and Nationality Act ( 8 U.S.C. 1451 ) is amended by adding at the end the following:\n(i) Any naturalized citizen who, after naturalization, is convicted of, or credibly found by the Secretary of Homeland Security to have participated in, any riot, unlawful protest involving violence or property destruction, or any act intended to overthrow or disrupt the constitutional order of the United States may be denaturalized and removed pursuant to expedited proceedings under section 238, regardless of the period of time elapsed since the date on which the citizen was naturalized. .\n#### 4. Expedited removal expansion\nSection 235(b) of the Immigration and Nationality Act ( 8 U.S.C. 1225(b) ) is amended\u2014\n**(1)**\nin paragraph (1)(A)(iii), by amending subclause (II) to read as follows:\n(II) Alien described An alien described in this subclause is an alien who has not been admitted or paroled into the United States and who is present in the United States without having been admitted or paroled, regardless of the period of time elapsed since the date on which such alien entered the United States. ; and\n**(2)**\nby adding at the end the following:\n(5) Applicability The Secretary of Homeland Security\u2014 (A) shall carry out expedited removal to the fullest extent permitted by this subsection; and (B) shall not grant any discretionary exception to such expedited removal except in a case involving a credible fear of persecution claim that is upheld after review. .\n#### 5. Mandatory comprehensive security review of certain nationals of Afghanistan admitted or paroled into the United States\n##### (a) In general\nThe Secretary of Homeland Security shall\u2014\n**(1)**\nconduct a comprehensive security review, including re-interviews and biometric checks, of each national of Afghanistan admitted as a refugee or pursuant to a special immigrant visa, or paroled into the United States, during the period beginning on January 20, 2021, and the date of the enactment of this Act; and\n**(2)**\nupon completion of such review, submit to Congress a certification of such completion.\n##### (b) Expedited removal for security risks\nAny individual subject to review under subsection (a) who the Secretary of Homeland Security determines poses a risk to national security or public safety shall be subject to expedited removal under section 235(b)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1225(b)(1) ).\n##### (c) Suspension of Afghan special immigrant visa and refugee processing\nEffective immediately, the processing of applications by nationals of Afghanistan for special immigrant or refugee status shall be suspended until the date on which the certification under subsection (a)(2) is submitted.\n##### (d) Limitation on funds for resettlement support\nNo Federal funds may be used for resettlement support for nationals of Afghanistan until the date on which the certification under subsection (a)(2) is submitted.\n#### 6. Termination of temporary protected status for high-risk nationals\nSection 244 of the Immigration and Nationality Act ( 8 U.S.C. 1254a ) is amended by adding at the end the following:\n(j) Automatic termination of status (1) In general The temporary protected status of nationals of a country designated under subsection (b) shall automatically terminate\u2014 (A) upon a finding by the Secretary of Homeland Security that conditions in such country no longer warrant such designation; or (B) on the date on which the Secretary submits a report under paragraph (2)(A)(ii) indicating that the crime rate among such nationals exceeds the national average crime rate by not less than 20 percent. (2) Semiannual crime rate calculation (A) In general Not later than 180 days after the date of the enactment of this subsection, and every 180 days thereafter, the Secretary of Homeland Security shall\u2014 (i) calculate\u2014 (I) the crime rate among nationals of each country designated under subsection (b); and (II) the national average crime rate; and (ii) submit a report to Congress that describes such crime rates. (B) Inclusion In calculating a crime rate under subparagraph (A)(i), the Secretary of Homeland Security shall include all offenses, including\u2014 (i) civil offenses; (ii) traffic violations; (iii) misdemeanors; and (iv) felonies. (3) Retroactive application Paragraph (1) shall apply retroactively to designations made under subsection (b) after January 20, 2021, including the designations of Afghanistan, Haiti, Venezuela, and Somalia. .",
      "versionDate": "2025-12-03",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-01-07T17:35:29Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3318is.xml"
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
      "title": "American Citizens First Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T06:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "American Citizens First Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T06:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to terminate Federal benefits for noncitizens, to authorize the denaturalization of naturalized citizens who undermine domestic tranquility, to expand expedited removal authority, to require mandatory revetting of nationals of Afghanistan, and to provide for automatic termination of temporary protected status, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T06:18:25Z"
    }
  ]
}
```
