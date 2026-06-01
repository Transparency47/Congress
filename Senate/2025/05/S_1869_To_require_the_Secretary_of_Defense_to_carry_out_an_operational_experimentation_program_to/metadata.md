# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1869?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1869
- Title: HOVER Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1869
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2025-06-20T12:45:57Z
- Update date including text: 2025-06-20T12:45:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1869",
    "number": "1869",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
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
    "title": "HOVER Act of 2025",
    "type": "S",
    "updateDate": "2025-06-20T12:45:57Z",
    "updateDateIncludingText": "2025-06-20T12:45:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-22",
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
          "date": "2025-05-22T16:34:12Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1869is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1869\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Cruz introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo require the Secretary of Defense to carry out an operational experimentation program to evaluate the military utility of optionally piloted vehicle rotary-wing aircraft, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Helicopter Operational Versatility and Enhanced Readiness Act of 2025 or the HOVER Act of 2025 .\n#### 2. Operational experimentation program for optionally piloted vehicle (OPV) rotary-wing aircraft\n##### (a) Operational experimentation program\nNot later than 180 days after the date of the enactment of this Act, the Secretary of the Army shall establish an operational experimentation program using optionally piloted vehicle (OPV) technology, including such rotary-wing platforms as the Secretary determines suitable\u2014\n**(1)**\nto evaluate the military utility of optionally piloted vehicle aircraft in contested environments;\n**(2)**\nto assess integration of such aircraft with crewed aircraft in multi-domain operations;\n**(3)**\nto analyze cost and maintenance benefits of autonomous flight;\n**(4)**\nto develop future tactics, techniques, and procedures (TTPs) for Army aviation; and\n**(5)**\nto complement and inform ongoing Army science and technology efforts relating to autonomy, such as the Autonomy for Combat Environment Sustainment (ACES), Mission Adaptive Autonomy (MAA), and the ALIAS transition agreement with the Defense Advance Research Projects Agency (DARPA).\n##### (b) Duration\nThe Secretary shall carry out the program required by subsection (a) during the two-year period beginning on the date of the commencement of the program.\n##### (c) Conversion\nUnder the program required by subsection (a), the Secretary shall convert at least three existing rotary-wing aircraft of the Army into optionally piloted vehicles.\n##### (d) Special use airspace\nThe Secretary shall ensure that all testing and evaluation under the program required by subsection (a) is conducted in special use airspace of the Department of Defense.\n##### (e) Program management\nThe Secretary shall carry out the program required by subsection (a) by acting through the Assistant Secretary of the Army for Acquisition, Logistics, and Technology in coordination with the head of the Program Executive Office for Aviation.\n##### (f) Partnerships\nIn carrying out the program required by subsection (a), the Secretary may collaborate with stakeholders in the United States defense industry, universities, and research institutions to advance optionally piloted vehicle technologies and integrate best practices to support rapid prototyping and ensure interoperability with broader Joint All-Domain Operations initiatives.\n##### (g) Report\nNot later than one year after the date of the enactment of this Act, the Secretary shall submit to the Committee on Armed Services of the Senate and the Committee on Armed Services of the House of Representatives a report detailing\u2014\n**(1)**\nprogress on the conversion required by subsection (c) and experimentation efforts under the program required by subsection (a);\n**(2)**\ninitial findings of the Secretary with respect to the program on operational efficiency, cost savings, and effectiveness; and\n**(3)**\nrecommendations for potential future procurement of optionally piloted vehicle platforms.\n##### (h) Implementation flexibility\nNothing in this section shall be construed to limit the ability of the Secretary to adjust the scope, platform selection, or methodology of experimentation to ensure alignment with existing service priorities and long-term modernization objectives.",
      "versionDate": "2025-05-22",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-20T12:45:57Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1869is.xml"
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
      "title": "HOVER Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-05T07:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "HOVER Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-05T07:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Helicopter Operational Versatility and Enhanced Readiness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-05T07:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Defense to carry out an operational experimentation program to evaluate the military utility of optionally piloted vehicle rotary-wing aircraft, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-05T07:48:17Z"
    }
  ]
}
```
