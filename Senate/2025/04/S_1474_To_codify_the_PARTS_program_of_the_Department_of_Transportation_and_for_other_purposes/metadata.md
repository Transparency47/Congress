# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1474?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1474
- Title: Vehicle Safety Research Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1474
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2025-09-29T15:27:11Z
- Update date including text: 2025-09-29T15:27:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1474",
    "number": "1474",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "P000595",
        "district": "",
        "firstName": "Gary",
        "fullName": "Sen. Peters, Gary C. [D-MI]",
        "lastName": "Peters",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Vehicle Safety Research Act of 2025",
    "type": "S",
    "updateDate": "2025-09-29T15:27:11Z",
    "updateDateIncludingText": "2025-09-29T15:27:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T20:16:22Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1474is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1474\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Peters (for himself and Mr. Young ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo codify the PARTS program of the Department of Transportation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Vehicle Safety Research Act of 2025 .\n#### 2. PARTS program\n##### (a) Definitions\nIn this section:\n**(1) External organization**\nThe term external organization means a nonprofit organization or institution of higher education with experience fulfilling contracts with Federal agencies\u2014\n**(A)**\nto carry out independent research; or\n**(B)**\nto administer federally-funded research and development centers.\n**(2) PARTS program**\nThe term PARTS program means the Partnership for Analytics Research in Traffic Safety (PARTS) program established by subsection (b).\n**(3) PARTS program participant**\nThe term PARTS program participant means an entity that has\u2014\n**(A)**\nvoluntarily chosen to participate in the PARTS program; and\n**(B)**\nbeen accepted as a participant in the PARTS program under the charter developed pursuant to subsection (b).\n**(4) Secretary**\nThe term Secretary means the Secretary of Transportation.\n##### (b) Establishment\nThere is established in the Department of Transportation a program, to be known as the Partnership for Analytics Research in Traffic Safety (PARTS) program , which shall be a continuation of the Partnership for Analytics Research in Traffic Safety (PARTS) program of the National Highway Traffic Safety Administration (as in effect on the day before the date of enactment of this Act).\n##### (c) Governance\nNot later than 180 days after the date of enactment of this Act, the Secretary, in consultation with PARTS program participants and any external organization that enters into a contract with the Secretary under subsection (d), shall develop a charter that shall govern the PARTS program.\n##### (d) PARTS program research\nThe Secretary shall enter into a contract with an external organization to conduct research to gather, analyze, and share certain traffic safety data and information pursuant to the PARTS program.\n##### (e) Information used for research pursuant to the parts program\nData submitted by PARTS program participants under the PARTS program shall be submitted in accordance with the charter developed under subsection (c), which shall, at minimum\u2014\n**(1)**\nensure that all data\u2014\n**(A)**\nremains under the ownership and control of the applicable PARTS program participant; and\n**(B)**\nexcept as provided in paragraph (2), is not accessible by any other entity other than an external organization that enters into a contract with the Secretary under subsection (d);\n**(2)**\nprevent PARTS program participant data or data analysis from being shared with any other PARTS program participant without express permission granted through a process agreed to pursuant to\u2014\n**(A)**\nthe charter developed under subsection (c); or\n**(B)**\na cooperative agreement entered into between a PARTS program participant and an external organization;\n**(3)**\ninstitute safeguards in data gathering and handling by an external organization pursuant to this subsection;\n**(4)**\nprevent reverse engineering aggregate data analysis results or other attempts to derive the identity of PARTS program participants from data analysis results;\n**(5)**\noutline the intended use of data analysis results, which shall only include\u2014\n**(A)**\nthe development, deployment, safety assessment, and regulation of safety technology; and\n**(B)**\nthe development of safety countermeasures; and\n**(6)**\nclarify that the participation of a PARTS program participant in the PARTS program does not affect or satisfy any other existing Federal regulatory requirements, including reporting requirements mandated by the National Highway Traffic Safety Administration.\n##### (f) Confidentiality\nPursuant to section 552(b)(3)(B) of title 5, United States Code, any report, data, communications between, work product, or other information voluntarily submitted to the Secretary or an external organization that enters into a contract with the Secretary under subsection (d) for purposes relating to conducting research pursuant to the PARTS program shall not be disclosed to the public.\n##### (g) Applicability of Paperwork Reduction Act\nSubchapter I of chapter 35 of title 44, United States Code (commonly known as the Paperwork Reduction Act ), shall not apply to any report, data, communication, work product, or other information gathered under the PARTS program.\n##### (h) No regulations required\nNotwithstanding any other provision of law, the Secretary shall not be required to promulgate any regulations to carry out the PARTS program.\n##### (i) Savings provision\nThis section shall not apply to any report, data, communication, work product, or other information\u2014\n**(1)**\nrequired to be submitted to the Secretary under any other provision of law; or\n**(2)**\notherwise available to the Secretary.\n##### (j) Authorization of appropriations\nThere are authorized to be appropriated to carry out the PARTS program\u2014\n**(1)**\nfor fiscal year 2026, $4,000,000;\n**(2)**\nfor fiscal year 2027, $6,000,000;\n**(3)**\nfor fiscal year 2028, $7,000,000;\n**(4)**\nfor fiscal year 2029, $8,000,000; and\n**(5)**\nfor fiscal year 2030, $9,000,000.",
      "versionDate": "2025-04-10",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-20T14:29:39Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s1474",
          "measure-number": "1474",
          "measure-type": "s",
          "orig-publish-date": "2025-04-10",
          "originChamber": "SENATE",
          "update-date": "2025-09-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1474v00",
            "update-date": "2025-09-29"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Vehicle Safety Research Act of 2025</strong></p><p>This bill provides statutory authority for the Partnership for\u00a0Analytics Research in Traffic Safety (PARTS) program in the National Highway Traffic Safety Administration (NHTSA). PARTS is an accord among\u00a0automakers\u00a0and NHTSA, which enables participants to voluntarily share safety-related data, via an independent third party, for collaborative safety analysis.</p><p>The bill specifies that</p><ul><li>NHTSA\u00a0must develop a governing charter for the program;\u00a0</li><li>NHTSA must contract with an external organization (i.e., a qualified nonprofit organization or institution of higher education) to conduct research to gather, analyze, and share certain traffic safety data and information;\u00a0and</li><li>any report, data, communications, work product, or other information voluntarily submitted to NHTSA or an external organization\u00a0under the program\u00a0shall not be disclosed to the public.</li></ul><p>Further, the bill specifies that NHTSA is not required to promulgate any regulations to carry out the PARTS program.</p>"
        },
        "title": "Vehicle Safety Research Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1474.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Vehicle Safety Research Act of 2025</strong></p><p>This bill provides statutory authority for the Partnership for\u00a0Analytics Research in Traffic Safety (PARTS) program in the National Highway Traffic Safety Administration (NHTSA). PARTS is an accord among\u00a0automakers\u00a0and NHTSA, which enables participants to voluntarily share safety-related data, via an independent third party, for collaborative safety analysis.</p><p>The bill specifies that</p><ul><li>NHTSA\u00a0must develop a governing charter for the program;\u00a0</li><li>NHTSA must contract with an external organization (i.e., a qualified nonprofit organization or institution of higher education) to conduct research to gather, analyze, and share certain traffic safety data and information;\u00a0and</li><li>any report, data, communications, work product, or other information voluntarily submitted to NHTSA or an external organization\u00a0under the program\u00a0shall not be disclosed to the public.</li></ul><p>Further, the bill specifies that NHTSA is not required to promulgate any regulations to carry out the PARTS program.</p>",
      "updateDate": "2025-09-29",
      "versionCode": "id119s1474"
    },
    "title": "Vehicle Safety Research Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Vehicle Safety Research Act of 2025</strong></p><p>This bill provides statutory authority for the Partnership for\u00a0Analytics Research in Traffic Safety (PARTS) program in the National Highway Traffic Safety Administration (NHTSA). PARTS is an accord among\u00a0automakers\u00a0and NHTSA, which enables participants to voluntarily share safety-related data, via an independent third party, for collaborative safety analysis.</p><p>The bill specifies that</p><ul><li>NHTSA\u00a0must develop a governing charter for the program;\u00a0</li><li>NHTSA must contract with an external organization (i.e., a qualified nonprofit organization or institution of higher education) to conduct research to gather, analyze, and share certain traffic safety data and information;\u00a0and</li><li>any report, data, communications, work product, or other information voluntarily submitted to NHTSA or an external organization\u00a0under the program\u00a0shall not be disclosed to the public.</li></ul><p>Further, the bill specifies that NHTSA is not required to promulgate any regulations to carry out the PARTS program.</p>",
      "updateDate": "2025-09-29",
      "versionCode": "id119s1474"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1474is.xml"
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
      "title": "Vehicle Safety Research Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-03T03:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Vehicle Safety Research Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to codify the PARTS program of the Department of Transportation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:18:29Z"
    }
  ]
}
```
