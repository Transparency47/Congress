# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3185?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3185
- Title: ANCHOR for Military Families Act
- Congress: 119
- Bill type: S
- Bill number: 3185
- Origin chamber: Senate
- Introduced date: 2025-11-18
- Update date: 2026-01-16T12:03:21Z
- Update date including text: 2026-01-16T12:03:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in Senate
- 2025-11-18 - IntroReferral: Introduced in Senate
- 2025-11-18 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-11-18: Introduced in Senate

## Actions

- 2025-11-18 - IntroReferral: Introduced in Senate
- 2025-11-18 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3185",
    "number": "3185",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "W000790",
        "district": "",
        "firstName": "Raphael",
        "fullName": "Sen. Warnock, Raphael G. [D-GA]",
        "lastName": "Warnock",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "ANCHOR for Military Families Act",
    "type": "S",
    "updateDate": "2026-01-16T12:03:21Z",
    "updateDateIncludingText": "2026-01-16T12:03:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-18",
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
      "actionDate": "2025-11-18",
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
        "item": [
          {
            "date": "2025-11-18T21:59:00Z",
            "name": "Referred To"
          },
          {
            "date": "2025-11-18T21:59:00Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "SD"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3185is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3185\nIN THE SENATE OF THE UNITED STATES\nNovember 18, 2025 Mr. Warnock (for himself and Mr. Rounds ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to require the Secretary of Defense to provide information on relocation assistance programs when a member of the Armed Forces receives orders for a change of permanent station, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Assuring Navigation of Compact Help for Ongoing Relocation for Military Families Act or the ANCHOR for Military Families Act .\n#### 2. Provision of Information Regarding Relocation Assistance Programs for Members Receiving Orders for a Change of Permanent Station\n##### (a) In General\nSection 1056 of title 10, United States Code, is amended\u2014\n**(1)**\nin subsection (b)(2)\u2014\n**(A)**\nin subparagraph (A), by striking and community orientation and inserting community orientation, education systems, school enrollment procedures, and State-specific provisions under the Interstate Compact on Educational Opportunity for Military Children ;\n**(B)**\nin subparagraph (C), by striking and community orientation and inserting community orientation, and educational resources for dependent children, including school transition assistance, academic continuity, and special education services ; and\n**(C)**\nby adding at the end the following new subparagraph:\n(E) Provision of educational planning and support services for dependent children with disabilities, including procedures for transferring individualized education programs and coordinating with the Exceptional Family Member Program. ;\n**(2)**\nby redesignating subsections (e) and (f) as subsections (f) and (g), respectively; and\n**(3)**\nby inserting after subsection (d) the following new subsection:\n(e) Provision of Information on Program (1) The Secretary of Defense shall ensure that members of the Armed Forces and the families of those members are provided information regarding available assistance under this section and any other assistance relating to a change of permanent station available under any other provision of law. (2) The Secretary shall ensure that information required to be provided under this subsection is provided to a member of the Armed Forces and the family of that member not later than 45 days before the date on which a change of permanent station takes effect for that member. (3) The information provided under this subsection shall include\u2014 (A) information on family assistance programs authorized under section 1788 of this title, including financial planning resources, spouse employment support, and community integration services; (B) guidance on available housing assistance, including on-base housing options, rental protections, and resources for off-base relocation; (C) mental health and well-being support services, including those accessible during the period of transition for a change of permanent station; (D) educational resources for dependent children, including school transition assistance and special education services; (E) information on available legal and financial counseling programs; and (F) any other assistance programs that support members of the Armed Forces and their families during relocation. (4) The Secretary of Defense shall\u2014 (A) incorporate the information required to be provided under this subsection into accessible materials and briefings provided to members of the Armed Forces relating to a change of permanent station; (B) ensure that the program under this section provides accessible materials and briefings at military installations and through online resources; (C) develop a communication strategy, including digital outreach and printed materials, to increase awareness of the program under this section and assistance available under other provisions of law relating to a change of permanent station; and (D) assess the satisfaction of members of the Armed Forces and their families with the information provided under this subsection. .\n##### (b) Report\nNot later than one year after the date of enactment of this Act, and annually thereafter for three years, the Secretary of Defense shall provide to the Committees on Armed Services of the Senate and the House of Representatives a briefing on the implementation of the amendments made by this section. Such briefing shall include\u2014\n**(1)**\nthe status of efforts to integrate information required to be provided by subsection (e) of section 1056 of title 10, United States Code, as added by subsection (a) of this section, into accessible materials and briefings provided to members of the Armed Forces and their families relating to a change of permanent station;\n**(2)**\nan assessment of the awareness by members of the Armed Forces and their families of available programs in support of a change of permanent station; and\n**(3)**\nany recommendations of the Secretary for improving the dissemination of information related to relocation and family assistance programs.",
      "versionDate": "2025-11-18",
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
        "actionDate": "2025-05-21",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "3566",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ANCHOR for Military Families Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-30",
        "text": "Received in the Senate."
      },
      "number": "3838",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Streamlining Procurement for Effective Execution and Delivery and National Defense Authorization Act for Fiscal Year 2026",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-02T20:50:03Z"
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
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3185is.xml"
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
      "title": "ANCHOR for Military Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T12:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ANCHOR for Military Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-02T05:08:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Assuring Navigation of Compact Help for Ongoing Relocation for Military Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-02T05:08:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 10, United States Code, to require the Secretary of Defense to provide information on relocation assistance programs when a member of the Armed Forces receives orders for a change of permanent station, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-02T05:03:18Z"
    }
  ]
}
```
