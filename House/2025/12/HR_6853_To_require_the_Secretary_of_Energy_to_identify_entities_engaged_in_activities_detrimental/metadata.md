# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6853?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6853
- Title: Securing Energy Supply Chains Act
- Congress: 119
- Bill type: HR
- Bill number: 6853
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-01-26T12:41:20Z
- Update date including text: 2026-01-26T12:41:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6853",
    "number": "6853",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "F000246",
        "district": "4",
        "firstName": "Pat",
        "fullName": "Rep. Fallon, Pat [R-TX-4]",
        "lastName": "Fallon",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Securing Energy Supply Chains Act",
    "type": "HR",
    "updateDate": "2026-01-26T12:41:20Z",
    "updateDateIncludingText": "2026-01-26T12:41:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6853ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6853\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Mr. Fallon introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Secretary of Energy to identify entities engaged in activities detrimental to the national security, economic security, or foreign policy of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Securing Energy Supply Chains Act .\n#### 2. Definitions\nIn this Act:\n**(1) Energy Non-Procurement List**\nThe term Energy Non-Procurement List means the list of identified entities established under section 3(a)(1).\n**(2) Foreign entity of concern**\nThe term foreign entity of concern has the meaning given the term in section 40207(a) of the Infrastructure Investment and Jobs Act ( 42 U.S.C. 18741(a) ).\n**(3) Secretary**\nThe term Secretary means the Secretary of Energy.\n#### 3. Energy non-procurement list\n##### (a) Establishment\n**(1) In general**\nNot later than 90 days after the date of enactment of this Act, the Secretary shall establish a list of identified entities that the Secretary has determined, based on the most recent information available, are engaged in activities detrimental to the national security, energy security, economic security, public safety, or foreign policy of the United States.\n**(2) Prioritization**\nIn carrying out paragraph (1), the Secretary shall prioritize identifying entities that produce, manufacture, process, extract, recycle, assemble, or otherwise provide\u2014\n**(A)**\ncritical materials (as defined in section 7002(a) of the Energy Act of 2020 ( 30 U.S.C. 1606(a) )); or\n**(B)**\nbatteries, including battery components.\n**(3) Inclusions**\nIn carrying out paragraph (1), the Secretary may include on the Energy Non-Procurement List\u2014\n**(A)**\nany entity that\u2014\n**(i)**\nis owned, controlled, or influenced by a foreign entity of concern;\n**(ii)**\nis included on the Chinese Military Company List of the Department of Defense published under section 1260H of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( 10 U.S.C. 113 note; Public Law 116\u2013283 );\n**(iii)**\nis included on the list of specially designated nationals and blocked persons maintained by the Office of Foreign Assets Control of the Department of the Treasury (commonly known as the SDN list );\n**(iv)**\nis included on the State Department list of foreign terrorist organizations; or\n**(v)**\nis included on the Consolidated Screening List maintained by the International Trade Administration of the Department of Commerce;\n**(B)**\nany entity that is a subsidiary or parent company of an entity included on the Energy Non-Procurement List under subparagraph (A); and\n**(C)**\nany other entity, as determined by the Secretary to be engaged in activities detrimental to the national security, economic security, or foreign policy of the United States.\n**(4) Annual revisions**\nThe Secretary shall, not less frequently than annually, make additions or deletions to the Energy Non-Procurement List.\n**(5) Consultation**\nIn carrying out paragraph (1), the Secretary may consult with the head of any appropriate Federal department or agency.\n##### (b) Report\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Secretary shall submit to the Committee on Energy and Natural Resources of the Senate and the Committee on Energy and Commerce of the House of Representatives a report containing\u2014\n**(A)**\nthe most up-to-date Energy Non-Procurement List; and\n**(B)**\na justification of why an entity was included on or removed from the Energy Non-Procurement List, as applicable.\n**(2) Form**\n**(A) Unclassified**\nThe information required under paragraph (1)(A) shall be submitted in unclassified form.\n**(B) Classified**\nThe information required under paragraph (1)(B) shall be submitted as a classified annex.\n**(3) Publication**\nConcurrent with the submission of a report described in paragraph (1), the Secretary shall publish the unclassified portion of that report on the website of the Department of Energy.\n#### 4. Prohibition on procurement\n##### (a) Prohibition\n**(1) In general**\nBeginning on the date that is 1 year after the date of the enactment of this Act\u2014\n**(A)**\nthe Secretary may not enter into or renew any DOE contract with a covered individual or entity unless the Secretary determines that the goods or services to be procured under such contract are not procurable from another source in the manner, time frame, or quantity required for the success of the applicable project; and\n**(B)**\na contractor of the Department of Energy (and any first-tier subcontractor thereof) may not enter into or renew a covered subcontract with a covered individual or entity unless the Secretary determines that the goods or services to be procured under such subcontract are not procurable from another source in the manner, time frame, or quantity required for the success of the applicable project.\n**(2) Certification**\nEach bidder or offeror for a DOE contract shall certify at the time of the submission of such bid or offer that the bidder or offeror is not a covered individual or entity.\n**(3) Contract termination**\nIn the case that the Secretary determines during the term of a DOE contract that the contractor (or subcontractor thereof at the first or second tier) is a covered individual or entity, the Secretary shall terminate the DOE contract unless the Secretary determines\u2014\n**(A)**\nthat the applicable goods or services are not procurable from another source in the manner, time frame, or quantity required for the success of the applicable project; or\n**(B)**\nwith respect to a subcontractor that is a covered individual or entity, the person that subcontracted with such subcontractor acted in good faith at such time in determining that the subcontractor was not a covered individual or entity.\n##### (b) Report\nNot later than 90 days after the date on which the Secretary enters into or renews a contract with a person under an exception provided by subsection (a)(1), the Secretary shall submit to the Committee on Energy and Natural Resources of the Senate and the Committee on Energy and Commerce of the House of Representatives a report that includes\u2014\n**(1)**\na description of the applicable contract;\n**(2)**\nan analysis of any existing alternative sources of the goods or services being procured in the applicable contract; and\n**(3)**\nrecommendations for how to support the development of domestic sources of those goods, services, or technologies, if those sources do not exist.\n##### (c) Definition\nIn this section:\n**(1) Covered individual or entity**\nThe term covered individual or entity means\u2014\n**(A)**\nan entity on the Energy Non-Procurement List; or\n**(B)**\nan individual or entity that provides funding to, or procures goods or services from an entity on the Energy Non-Procurement List.\n**(2) DOE contract**\nThe term DOE contract means a contract with the Department of Energy for the procurement of goods or services.\n**(3) Subcontract**\nThe term subcontract means a subcontract for an amount exceeding $250,000.\n#### 5. List overlap study\n##### (a) Study\nNot later than 1 year after the date of enactment of this Act, the Secretary, in coordination with the Secretary of Commerce, the Secretary of Defense, the Secretary of State, the Secretary of the Treasury, the Director of National Intelligence, and the heads of other Federal departments and agencies, as the Secretary determines appropriate, shall carry out a study to identify lists created by each Federal department or agency, and any overlap present when comparing those lists, relating to\u2014\n**(1)**\nforeign entities of concern;\n**(2)**\nentities subject to sanctions imposed by the United States;\n**(3)**\nChinese military companies;\n**(4)**\nentities with which Federal agencies are prohibited from entering into procurement contracts; and\n**(5)**\nother entities that work with the Chinese Communist Party.\n##### (b) Report\nNot later than 1 year after the date of enactment of this Act, the Secretary shall submit to Congress a report that includes\u2014\n**(1)**\nthe results of the study conducted under subsection (a); and\n**(2)**\nrecommendations on how to harmonize the lists identified in the study conducted under subsection (a) in order to provide clarification on which entities the Federal Government should not contract with to procure goods, services, or technology.",
      "versionDate": "2025-12-18",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Energy",
        "updateDate": "2026-01-26T12:41:19Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6853ih.xml"
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
      "title": "Securing Energy Supply Chains Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Securing Energy Supply Chains Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Energy to identify entities engaged in activities detrimental to the national security, economic security, or foreign policy of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:31Z"
    }
  ]
}
```
