# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1242?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1242
- Title: Watershed Results Act
- Congress: 119
- Bill type: S
- Bill number: 1242
- Origin chamber: Senate
- Introduced date: 2025-04-01
- Update date: 2026-04-08T15:43:03Z
- Update date including text: 2026-04-08T15:43:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-04-01: Introduced in Senate
- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.
- Latest action: 2025-04-01: Introduced in Senate

## Actions

- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1242",
    "number": "1242",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "W000779",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Wyden, Ron [D-OR]",
        "lastName": "Wyden",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Watershed Results Act",
    "type": "S",
    "updateDate": "2026-04-08T15:43:03Z",
    "updateDateIncludingText": "2026-04-08T15:43:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-01",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T21:54:06Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-17T14:00:02Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
      "systemCode": "sseg00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1242is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1242\nIN THE SENATE OF THE UNITED STATES\nApril 1 (legislative day, March 31), 2025 Mr. Wyden introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo authorize the Secretary of the Interior to carry out watershed pilots, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Watershed Results Act .\n#### 2. Definitions\nIn this Act:\n**(1) Advance watershed analytics**\nThe term advance watershed analytics means the technical analysis that\u2014\n**(A)**\nis conducted before providing funding for a watershed outcomes project;\n**(B)**\nidentifies and quantifies the outcomes and costs of all potential qualifying activities across the watershed outcomes project; and\n**(C)**\nassesses how different groups of qualifying activities in the watershed outcomes project could efficiently maximize outcomes for the least cost.\n**(2) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Energy and Natural Resources of the Senate; and\n**(B)**\nthe Committee on Natural Resources of the House of Representatives.\n**(3) Eligible entity**\nThe term eligible entity includes\u2014\n**(A)**\na State, Indian Tribe, Tribal organization, irrigation district, or water district;\n**(B)**\na State, regional, or local authority, the members of which include 1 or more organizations with water or power delivery authority;\n**(C)**\nany other organization with water or power delivery authority; and\n**(D)**\nany nongovernmental entity.\n**(4) Pay-for-performance contract**\nThe term pay-for-performance contract means a contract to purchase verified outcomes produced by implemented qualifying activities in a watershed outcomes project at a negotiated price.\n**(5) Qualifying activity**\nThe term qualifying activity means a conservation project carried out in a watershed identified through advance watershed analytics as having a high likelihood of cost-effectively achieving 1 or more outcomes if implement consistent with applicable performance standards made available under section 3(e)(4).\n**(6) Reclamation State**\nThe term Reclamation State means\u2014\n**(A)**\na State or territory described in the first section of the Act of June 17, 1902 (32 Stat. 388, chapter 1093; 43 U.S.C. 391 );\n**(B)**\nthe State of Hawaii;\n**(C)**\nthe State of Alaska; and\n**(D)**\nthe Commonwealth of Puerto Rico.\n**(7) Secretary**\nThe term Secretary means the Secretary of the Interior, acting through the Commissioner of Reclamation.\n**(8) Watershed outcomes project**\nThe term watershed outcomes project means the overall watershed project managed by the watershed partner.\n**(9) Watershed partner**\nThe term watershed partner means an eligible entity selected by the Secretary under section 3(a)(2) to carry out a watershed outcomes project.\n#### 3. Watershed outcomes projects\n##### (a) Proposals; selection\nThe Secretary shall\u2014\n**(1)**\nnot later than 1 year after the date of enactment of this Act, solicit the submission from eligible entities of proposals to develop and implement a strategy that develops and uses advance watershed analytics to cost-effectively carry out watershed outcomes projects to achieve meaningful watershed-scale outcomes in a Reclamation State; and\n**(2)**\nfrom among the proposals submitted under paragraph (1), select a watershed partner for each watershed to complete advance watershed analytics, carry out watershed outcomes projects in a Reclamation State, manage watershed partnership duties during the term of the partnership agreement, and support pay-for-performance contracts.\n##### (b) Guidelines and criteria for proposals\nThe Secretary\u2014\n**(1)**\nshall develop criteria and guidelines for the submission and selection of proposals under subsection (a); and\n**(2)**\nfor purposes of developing the criteria and guidelines under paragraph (1), may consider\u2014\n**(A)**\nthe scope of the proposed watershed outcomes project, including the selected subregion or basin-level watershed for consideration;\n**(B)**\nthe purpose and goals of the proposed watershed outcomes project;\n**(C)**\nany stakeholder outreach conducted with respect to the proposed watershed outcomes project;\n**(D)**\nevidence of widespread support within the local community for, the proposed watershed outcomes project;\n**(E)**\nthe capability of the watershed partner to perform the required duties in accordance with subsection (d);\n**(F)**\nhow the watershed partner will procure and use advance watershed analytics to identify and quantify the outcomes and costs of all potential qualifying activities for the proposed watershed outcomes project;\n**(G)**\nestimated costs of completing advance watershed analytics and operating the proposed watershed outcomes project;\n**(H)**\nthe anticipated qualifying activity types that are relevant for the selected watershed identified under subparagraph (A); and\n**(I)**\nplans for monitoring, evaluating, and reporting on progress made toward achieving the outcomes of the proposed watershed outcomes project.\n##### (c) Partnership agreements\n**(1) In general**\nThe Secretary may enter into a partnership agreement with a watershed partner selected under subsection (a)(2) to design and implement a watershed outcomes project that uses advance watershed analytics to achieve meaningful watershed-scale outcomes in accordance with this section.\n**(2) Term**\n**(A) In general**\nA partnership agreement entered into under paragraph (1) shall be for a term\u2014\n**(i)**\nof not more 5 years; or\n**(ii)**\nif the Secretary determines that a longer term is necessary to meet the objectives of the watershed outcomes project, a longer term established by the Secretary.\n**(B) Renewal**\nA partnership agreement entered into under paragraph (1) may be renewed for a term of not more than 5 years.\n**(C) Extension**\nA partnership agreement entered into under paragraph (1) or renewed under subparagraph (B) may be extended 1 time for a term of not more than 2 years, as determined by the Secretary.\n**(3) Technical and financial assistance**\nThrough a partnership agreement entered into under paragraph (1), the Secretary shall provide to a watershed partner\u2014\n**(A)**\ntechnical or financial assistance to design and implement a watershed outcomes project; and\n**(B)**\ngrants, cooperative agreements, or other financial assistance to support\u2014\n**(i)**\nthe activities under subparagraph (A); and\n**(ii)**\nperformance payments to qualifying activities under subsection (g)(4).\n**(4) Project development costs**\nThe Secretary may annually award to a watershed partner an amount equal to not more than 50 percent of estimated costs of the watershed outcomes project to carry out the duties described in subsection (d).\n##### (d) Duties of watershed partners\nUnder a partnership agreement entered into under subsection (c)(1), the Secretary shall establish duties to be carried out by the watershed partner, including considering establishing the following duties:\n**(1)**\nPreparing a funding and implementation strategy that uses advance watershed analytics to cost-effectively carry out a watershed outcomes project by selecting a sufficient number of qualifying activities to achieve meaningful watershed-scale outcomes by\u2014\n**(A)**\ncompleting advance watershed analytics to identify and quantify the outcomes and costs of all potential qualifying activities for the watershed outcomes project;\n**(B)**\nestablishing baseline metrics to support the development of setting outcome prices and performance standards for the watershed outcomes project;\n**(C)**\ndeveloping performance standards for the watershed outcomes project;\n**(D)**\nleveraging financial assistance provided by the Secretary to secure additional funds for the watershed outcomes project;\n**(E)**\ndesigning, recruiting, and verifying qualifying activities for the watershed outcomes project; and\n**(F)**\nproviding outcome and financial accounting services relating to qualifying activities carried out to achieve outcomes.\n**(2)**\nUsing the strategy prepared under paragraph (1) to prioritize qualifying activity outreach efforts.\n**(3)**\nWorking with local stakeholders to recruit and design an implementation-ready queue of priority qualifying activities.\n**(4)**\nEnsuring that any proposed priority qualifying activities have the support of affected local stakeholders.\n**(5)**\nSetting activity outcome prices and developing performance standards for qualifying activities.\n**(6)**\nDeveloping a plan to carry out qualifying activities having a high likelihood of cost-effectively achieving 1 or more outcomes described in subsection (f) if implemented consistent with the applicable performance standards made available by the Secretary under subsection (e)(4).\n**(7)**\nSelecting, developing pay-for-performance contracts for, funding, and carrying out qualifying activities, in accordance with the plan developed under paragraph (6), to achieve meaningful watershed-scale outcomes.\n**(8)**\n**(A)**\nQuantifying the outcomes for qualifying activities.\n**(B)**\nVerifying that qualifying activities have been implemented consistent with applicable performance standards.\n**(C)**\nProviding applicable documentation to the Secretary with respect to the information quantified and verified under subparagraphs (A) and (B).\n**(9)**\nMonitoring qualifying activities at appropriate levels to confirm ongoing performance.\n**(10)**\nOther duties necessary to carry out a watershed outcomes project, as determined to be necessary by the Secretary.\n##### (e) Duties of Secretary\nUnder a partnership agreement entered into under subsection (c), the Secretary shall\u2014\n**(1)**\nensure that there is widespread support within the local community for the watershed outcomes project;\n**(2)**\nverify the advance watershed analytics completed by the watershed partner, to the maximum extent practicable;\n**(3)**\nensure that there are made available to the public outcome price tables, by qualifying activity type, for use as the basis for negotiating pay-for-performance contracts for the applicable watershed outcomes project;\n**(4)**\nensure that there are made available to the public qualifying activity and watershed outcomes project performance standards that are to be used as the basis for\u2014\n**(A)**\nidentifying, quantifying, and verifying qualifying activity outcomes; and\n**(B)**\nexecuting pay-for-performance contracts;\n**(5)**\nreview outcome quantification and verification documentation provided by the watershed partner under subsection (d)(8)(C);\n**(6)**\nprovide to a watershed partner financial assistance to purchase verified outcomes from qualifying activities in a watershed outcomes project, at prices set for the watershed outcomes project in accordance with this section; and\n**(7)**\ncoordinate with other Federal agencies, to the maximum extent practicable, to help leverage and concentrate funding into watershed outcomes projects.\n##### (f) Required outcomes for qualifying activities\nTo be eligible for a performance payment under subsection (g)(4), a qualified activity shall produce 1 or more measurable, clearly defined outcomes that result in a quantifiable and verifiable\u2014\n**(1)**\nincrease in surface water or groundwater;\n**(2)**\nincrease in aquatic habitat quality, quantity, connectivity, or access in a watershed;\n**(3)**\nsurface water or groundwater quality improvement, including water temperature reductions, or a reduction in salinity or nutrient or sediment runoff associated with irrigated agriculture; or\n**(4)**\nother quantifiable benefits, as determined by the Secretary, likely to improve watershed health in the watershed outcomes project.\n##### (g) Financial assistance for qualifying activities in watershed outcomes projects\n**(1) Leveraging Federal funding**\nTo achieve meaningful watershed-scale outcomes, amounts made available under section 5 may be used to satisfy any cost-sharing requirement with respect to carrying out a watershed outcomes project.\n**(2) Federal share**\nThe Federal share of grants or other financial assistance for a watershed outcomes project under this Act shall be not more than 75 percent of the total cost of the watershed outcomes project.\n**(3) Watershed partner contributions**\nThe Secretary may\u2014\n**(A)**\naccept non-Federal contributions for a watershed outcomes project, including funding or financing secured by the watershed partner in accordance with the strategy developed under subsection (d)(1); and\n**(B)**\nuse amounts accepted under subparagraph (A) to carry out activities authorized under this Act in the watershed outcomes project.\n**(4) Performance payments**\nNot later than 90 days after the date on which a watershed partner verifies the outcomes generated from qualifying activities and confirms that the qualifying activity has been implemented consistent with the performance standards of the applicable watershed outcomes project, the Secretary shall provide financial assistance to the watershed partner to support performance payments.\n##### (h) Maximum number of watershed outcomes projects\nNot more than a total of 5 watershed outcomes projects may be carried out under this section.\n##### (i) Restrictions on use of advance watershed analytics data\n**(1) In general**\nNothing in this Act affects or modifies existing law with respect to the treatment of personal data in the conduct by an employee of the Federal Government or a designee of an employee of the Federal Government in carrying out official duties of the Federal employee or designee under this Act.\n**(2) Data collection**\nAll information or data collected or assembled by a Federal employee or a designee of a Federal employee to complete advance watershed analytics activities, directly or indirectly, under this Act\u2014\n**(A)**\nshall be used for the sole purpose of identifying, prioritizing, and funding qualifying activities in a watershed outcomes project; and\n**(B)**\nshall be considered to be confidential commercial information that is exempt from disclosure under section 552(b)(4) of title 5, United States Code (commonly known as the Freedom of Information Act ).\n**(3) Applicability to watershed partners**\nAny restrictions on a Federal employee under this section shall apply to an employee of a watershed partner.\n##### (j) Effect\nNothing in this Act creates, impairs, alters, or supersedes a Federal or State water right.\n#### 4. Briefing; Reports\n##### (a) Annual briefing or report\nFor each fiscal year for which a watershed outcomes project is carried out under section 3, not later than the date on which the budget of the United States Government is submitted by the President under section 1105 of title 31, United States Code, for that fiscal year, the Secretary shall provide to the appropriate committees of Congress a briefing or report describing the status of each watershed outcomes project, including progress towards the applicable strategy prepared under section 3(d)(1), including any payments made for outcomes.\n##### (b) 5 -Year report\nNot later than October 1 of the fifth fiscal year in which a watershed outcomes project is carried out under section 3, the Secretary shall submit to the appropriate committees of Congress a report that\u2014\n**(1)**\nsummarizes\u2014\n**(A)**\nthe projected results of the qualifying activities in the watershed outcomes project in meeting the strategy prepared under section 3(d)(1);\n**(B)**\nthe projected outcomes of the watershed outcomes project;\n**(C)**\nthe total amount of funds secured for the watershed outcomes project;\n**(D)**\nthe type of funding expended under the watershed outcomes project; and\n**(E)**\nsuch other information as the Secretary determines to be appropriate; and\n**(2)**\nincludes recommendations for continuing, terminating, or making permanent the authorizations under this Act.\n#### 5. Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out this Act $17,000,000 for each of fiscal years 2026 through 2031.",
      "versionDate": "2025-04-01",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2026-03-18T13:28:10Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-08T15:43:02Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2026-03-18T13:28:10Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-03-18T13:28:10Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2026-03-18T13:28:10Z"
          },
          {
            "name": "Wages and earnings",
            "updateDate": "2026-03-18T13:28:10Z"
          },
          {
            "name": "Water resources funding",
            "updateDate": "2026-03-18T13:28:10Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2026-03-18T13:28:10Z"
          },
          {
            "name": "Watersheds",
            "updateDate": "2026-03-18T13:28:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2025-05-28T14:24:27Z"
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
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1242is.xml"
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
      "title": "Watershed Results Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Watershed Results Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the Secretary of the Interior to carry out watershed pilots, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T03:03:33Z"
    }
  ]
}
```
