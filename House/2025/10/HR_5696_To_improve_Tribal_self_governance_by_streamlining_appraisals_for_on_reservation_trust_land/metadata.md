# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5696?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5696
- Title: STREAMLINE ACT
- Congress: 119
- Bill type: HR
- Bill number: 5696
- Origin chamber: House
- Introduced date: 2025-10-06
- Update date: 2026-01-14T19:53:28Z
- Update date including text: 2026-01-14T19:53:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-10-06: Introduced in House
- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-11-12 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2025-11-19 - Committee: Subcommittee Hearings Held
- Latest action: 2025-10-06: Introduced in House

## Actions

- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-11-12 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2025-11-19 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-06",
    "latestAction": {
      "actionDate": "2025-10-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5696",
    "number": "5696",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "L000578",
        "district": "1",
        "firstName": "Doug",
        "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
        "lastName": "LaMalfa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "STREAMLINE ACT",
    "type": "HR",
    "updateDate": "2026-01-14T19:53:28Z",
    "updateDateIncludingText": "2026-01-14T19:53:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-12",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Indian and Insular Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-06",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-10-06T19:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-11-19T15:15:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-11-12T21:42:31Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "systemCode": "hsii00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5696ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5696\nIN THE HOUSE OF REPRESENTATIVES\nOctober 6, 2025 Mr. LaMalfa introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo improve Tribal self-governance by streamlining appraisals for on-reservation trust land acquisitions by Indian Tribes with self-governance realty programs.\n#### 1. Short title\nThis Act may be cited as the Strengthening Tribal Real Estate Authority and Modernizing Land for Indigenous Nation Expansion Act or the STREAMLINE ACT .\n#### 2. Regulatory revision to part 151 of title 25, Code of Federal Regulations\n##### (a) Definitions\nIn this section:\n**(1) ISDEAA**\nThe term ISDEAA means the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5301 et seq. ).\n**(2) Self-governance realty program**\nThe term self-governance realty program means a program operated by an Indian Tribe under a compact or funding agreement pursuant to title I or title IV of ISDEAA that includes real estate services and valuation functions recognized by the Office of Tribal Sovereignty of the Department of the Interior.\n**(3) Indian Tribe**\nThe term Indian Tribe has the meaning of the term Indian tribe in section 102 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5130 ).\n**(4) Secretary**\nThe term Secretary means the Secretary of the Interior.\n**(5) Tribal appraisal**\nThe term Tribal appraisal means a valuation prepared for an Indian Tribe by personnel or contractors operating under the Indian Tribe\u2019s ISDEAA title I contract or ISDEAA title IV compact or funding agreement in conformance with the Uniform Standards of Professional Appraisal Practice.\n##### (b) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary shall revise part 151 of title 25, Code of Federal Regulations (relating to land acquisitions), to provide that the Secretary shall accept a Tribal appraisal or valuation in lieu of a Federal appraisal with respect to an Indian Tribe if\u2014\n**(1)**\nthe Indian Tribe is party to an ISDEAA title I of contract or ISDEAA title IV compact or funding agreement;\n**(2)**\nthe Indian Tribe has assumed responsibility for realty or land management functions under such contract, compact, or funding agreement, including the authority to conduct appraisals or valuations; and\n**(3)**\nthe land to be acquired is located within the exterior boundaries of the reservation of the Indian Tribe, or contiguous to lands held in trust for the Indian Tribe.\n##### (c) Appraisal acceptance\nNot later than 1 year after the date of the enactment of this Act, the Secretary shall revise part 151 of title 25, Code of Federal Regulations, to provide that, for acquisitions within a reservation or contiguous to trust lands of an Indian Tribe, the Secretary shall accept a Tribal appraisal in lieu of an appraisal procured or reviewed by the Appraisal and Valuation Services Office, if\u2014\n**(1)**\nthe Indian Tribe is party to an ISDEAA title I of contract or ISDEAA title IV compact or funding agreement;\n**(2)**\nthe contract, compact, or funding agreement includes real estate services and valuation authority; and\n**(3)**\nthe appraisal conforms to the Uniform Standards of Professional Appraisal Practice.\n##### (d) Indian Trust Asset Reform\nNothing in this section limits Indian Tribes from using the authorities available to Indian Tribes under section 305 of the Indian Trust Asset Reform Act ( 25 U.S.C. 5635 ).\n##### (e) Fiduciary and trust duty satisfied\nAcceptance by the Secretary of a Tribal appraisal that meets the requirements of subsection (b) shall be deemed in compliance with the Secretary\u2019s fiduciary and trust responsibility with respect to valuation for such acquisition.\n##### (f) Ministerial role\nIn the case of the acceptance of Tribal appraisal pursuant to subsection (b), the role of the Department of the Interior shall be limited to ministerial confirmation of receipt and recordation of the Tribal certification.\n##### (g) Policy manuals\nThe Secretary shall conform relevant Department of the Interior manuals, including the Appraisal and Valuation Services Office guidance and the Fee-to-Trust Handbook (52 IAM 12\u2013H), to the requirements of subsection (b).\n#### 3. Amendment to Indian Land Consolidation Act\nSection 219 of the Indian Land Consolidation Act ( 25 U.S.C. 2218 ) is amended by adding at the end the following:\n(h) Tribal appraisals under self-Governance realty programs Notwithstanding any other provision of law, the Secretary\u2014 (1) shall not require an appraisal prepared by or reviewed by the Department of the Interior for a conveyance or acquisition of trust or restricted land by an Indian tribe, if\u2014 (A) the tribe is a party to a self-governance compact or contract under title I or title IV of the Indian Self-Determination and Education Assistance Act; (B) the tribe has assumed responsibility for realty or land management functions under such compact or contract, including the authority to conduct appraisals or valuations; (C) the land is located within the exterior boundaries of the tribe\u2019s reservation, or contiguous to lands already held in trust for the tribe; and (D) the appraisal conforms to Uniform Standards of Professional Appraisal Practice; and (2) if the criteria described in subparagraphs (A) through (D) of paragraph (1) are met, shall accept appraisals or valuations conducted under the tribe\u2019s compacted program as sufficient to establish fair market value. .\n#### 4. Transparency and evaluation\n##### (a) Data\nThe Secretary shall track and publish processing times for fee-to-trust acquisitions using Tribal appraisals versus Department of the Interior appraisals.\n##### (b) Report\nNot later than 3 years after the date of the enactment of this Act, the Comptroller General shall evaluate the implementation of this Act and any effects on processing time, quality, and litigation.\n##### (c) No effect on NEPA or title review\nNothing in this Act alters requirements for environmental compliance, title evidence, or notice under part 151 of title 25, Code of Federal Regulations.",
      "versionDate": "2025-10-06",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Federal-Indian relations",
            "updateDate": "2026-01-14T19:53:24Z"
          },
          {
            "name": "Indian lands and resources rights",
            "updateDate": "2026-01-14T19:53:19Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2026-01-14T19:53:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-12-04T21:40:01Z"
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
      "date": "2025-10-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5696ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "STREAMLINE ACT",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T06:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STREAMLINE ACT",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T06:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strengthening Tribal Real Estate Authority and Modernizing Land for Indigenous Nation Expansion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T06:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve Tribal self-governance by streamlining appraisals for on-reservation trust land acquisitions by Indian Tribes with self-governance realty programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T06:18:23Z"
    }
  ]
}
```
