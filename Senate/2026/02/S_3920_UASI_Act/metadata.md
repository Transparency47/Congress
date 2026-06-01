# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3920?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3920
- Title: UASI Act
- Congress: 119
- Bill type: S
- Bill number: 3920
- Origin chamber: Senate
- Introduced date: 2026-02-25
- Update date: 2026-03-16T17:53:50Z
- Update date including text: 2026-03-16T17:53:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-25: Introduced in Senate
- 2026-02-25 - IntroReferral: Introduced in Senate
- 2026-02-25 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-02-25: Introduced in Senate

## Actions

- 2026-02-25 - IntroReferral: Introduced in Senate
- 2026-02-25 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3920",
    "number": "3920",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "UASI Act",
    "type": "S",
    "updateDate": "2026-03-16T17:53:50Z",
    "updateDateIncludingText": "2026-03-16T17:53:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-25",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-25",
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
          "date": "2026-02-25T20:12:44Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3920is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3920\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2026 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo strengthen homeland security by expanding Urban Areas Security Initiative grant eligibility criteria to promote cooperation with U.S. Immigration and Customs Enforcement and to advance election security protections.\n#### 1. Short titles\nThis Act may be cited as the Unifying American Security Interests Act or the UASI Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Urban Areas Security Initiative provides critical funding to high-risk urban areas to enhance preparedness against terrorism and other threats under the Homeland Security Grant Program.\n**(2)**\nEffective border security and immigration enforcement are integral to national homeland security, requiring collaboration between Federal, State, local, Tribal, and territorial entities.\n**(3)**\nThe fiscal year 2025 Homeland Security Grant Program Notice of Funding Opportunity established National Priority Areas to address emerging threats, including support for border crisis response through cooperation with U.S. Immigration and Customs Enforcement.\n**(4)**\nCodifying the requirements referred to in paragraphs (1) through (3) will ensure consistent application and prevent future circumvention through administrative or judicial actions.\n#### 3. Eligibility for Urban Areas Security Initiative grants\nSection 2008 of the Homeland Security Act of 2002 ( 6 U.S.C. 609 ) is amended by adding at the end the following:\n(h) Eligibility for Urban Areas Security Initiative grants (1) National priority areas requirement As a condition of eligibility for a grant under the Urban Areas Security Initiative, each applicant (including State administrative agencies and eligible urban areas) shall demonstrate in its application that it will allocate not less than 30 percent of the total award amount across the following National Priority Areas: (A) Enhancing cybersecurity. (B) Enhancing the protection of soft targets and crowded places. (C) Supporting Homeland Security Task Forces and Fusion Centers. (D) Enhancing election security. (E) Supporting border crisis response and enforcement. (2) Minimum allocations Of the amount required to be allocated under paragraph (1)\u2014 (A) not less than 3 percent of the total award shall be dedicated to activities in support of enhancing election security; and (B) not less than 10 percent of the total award shall be dedicated to activities that supporting border crisis response and enforcement, which shall include\u2014 (i) participating in the program authorized under section 287(g) of the Immigration and Nationality Act ( 8 U.S.C. 1357(g) ), including training and authorizing local officers to perform immigration enforcement functions such as identifying and processing removable noncitizens in their custody; (ii) cooperating with detainers received from U.S. Immigration and Customs Enforcement and other jurisdictional responsibilities related to immigration enforcement; (iii) training for law enforcement personnel in immigration law, civil rights protections, and procedures under the program referred to in clause (i); (iv) developing information-sharing platforms or secure networks between local agencies and U.S. Immigration and Customs Enforcement; (v) procuring technology for screening, detection, and communications to support immigration enforcement; (vi) participating in joint training exercises with U.S. Immigration and Customs Enforcement to improve coordination; and (vii) staffing and operational overtime directly tied to activities described in clause (i), such as expanding screening in correctional facilities. (3) Investment justification and coordination Each applicant for a grant under the Urban Areas Security Initiative shall submit to the Secretary of Homeland Security a dedicated investment justification for projects that supporting border crisis response and enforcement that details alignment with border security goals. All such projects shall require coordination with U.S. Immigration and Customs Enforcement field offices. (4) Compliance certifications Each applicant for a grant under the Urban Areas Security Initiative shall certify to the Secretary of Homeland Security that funded activities will comply with all applicable Department of Homeland Security terms, including prohibitions on benefitting or incentivizing illegal immigration. (5) Noncompliance penalties Failure of a grantee to meet the minimum allocations required under this subsection may result in the Secretary of Homeland Security\u2014 (A) denying eligibility for a grant under the Urban Areas Security Initiative; (B) placing a hold on up to 30 percent of the award until such failure is remedied; or (C) imposing another remedy, including award termination or debarment of the grantee from future grants. (6) Applicability The requirements under this subsection shall apply to all Urban Areas Security Initiative grants awarded for fiscal year 2027 or for any fiscal year thereafter. .\n#### 4. Rule of construction\nNothing in this Act may be construed to preempt State or local laws, except to the extent necessary to ensure compliance with the conditions for Federal grant funding established under section 2008(h) of the Homeland Security Act of 2002 ( 6 U.S.C. 609(h) ), as added by section 3.",
      "versionDate": "2026-02-25",
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
        "updateDate": "2026-03-16T17:53:50Z"
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
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3920is.xml"
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
      "title": "UASI Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-13T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "UASI Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-13T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Unifying American Security Interests Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-13T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to strengthen homeland security by expanding Urban Areas Security Initiative grant eligibility criteria to promote cooperation with U.S. Immigration and Customs Enforcement and to advance election security protections.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-13T03:48:21Z"
    }
  ]
}
```
