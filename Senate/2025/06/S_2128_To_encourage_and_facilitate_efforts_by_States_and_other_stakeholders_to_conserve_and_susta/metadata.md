# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2128?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2128
- Title: MONARCH Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2128
- Origin chamber: Senate
- Introduced date: 2025-06-18
- Update date: 2026-04-06T16:35:35Z
- Update date including text: 2026-04-06T16:35:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-18: Introduced in Senate
- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-06-18: Introduced in Senate

## Actions

- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-18",
    "latestAction": {
      "actionDate": "2025-06-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2128",
    "number": "2128",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "MONARCH Act of 2025",
    "type": "S",
    "updateDate": "2026-04-06T16:35:35Z",
    "updateDateIncludingText": "2026-04-06T16:35:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-18",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-18",
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
          "date": "2025-06-18T18:43:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "RI"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "NM"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "OR"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "IL"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "MD"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "CA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2128is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2128\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. Merkley (for himself, Mr. Whitehouse , Mr. Heinrich , Mr. Wyden , Ms. Duckworth , Mr. Van Hollen , Mr. Padilla , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo encourage and facilitate efforts by States and other stakeholders to conserve and sustain the western population of monarch butterflies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Monarch Action, Recovery, and Conservation of Habitat Act of 2025 or the MONARCH Act of 2025 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nthe population of western monarch butterflies is at imminent risk of extinction;\n**(2)**\nover the past 3 decades, the population of western monarch butterflies has declined by more than 99 percent due to prolonged drought, loss of milkweed and native pollinator habitat, loss of breeding and overwintering habitat, and climate change;\n**(3)**\nin 2020, the population of western monarch butterflies reached a new historic low of 1,914 butterflies, falling below the predicted extinction threshold for the third year in a row;\n**(4)**\nin 2024, the population of western monarch butterflies reached the second lowest on record, with less than 10,000 butterflies recorded;\n**(5)**\nthe extinction of the population of migratory western monarch butterflies is now likely to occur within the next 2 decades if urgent action is not taken;\n**(6)**\nactively restoring native milkweed and nectar plants, monarch overwintering habitat, and other pollinator habitat, and ensuring that key habitats are protected from destruction, are critical to ensuring the survival of western monarch butterflies and can also help facilitate conservation of other essential pollinators; and\n**(7)**\nenhancing pollinator populations can result in improved pollination services for neighboring land, including agriculture and wildlife ecosystems.\n#### 3. Definitions\nIn this Act:\n**(1) Conservation**\nThe term conservation means the use of each method or procedure necessary to protect habitats of western monarch butterflies and other pollinators within the range of western monarch butterflies, including\u2014\n**(A)**\nthe protection, restoration, and management of overwintering, breeding, and migratory habitats;\n**(B)**\nassistance in the development and implementation of national, regional, State, Tribal, and local conservation and management plans; and\n**(C)**\ncommunity outreach and education.\n**(2) Fund**\nThe term Fund means the Western Monarch Butterfly Rescue Fund established by section 5(a).\n**(3) Secretary**\nThe term Secretary means the Secretary of the Interior.\n**(4) Tribal government**\nThe term Tribal government means the governing body of a federally recognized Indian Tribe.\n**(5) Western monarch butterfly**\nThe term western monarch butterfly means the monarch butterfly population that overwinters along the coast of the State of California and breeds across the States of California, Arizona, Nevada, Washington, Oregon, Idaho, and Utah.\n#### 4. Western monarch butterfly conservation grant program\n##### (a) In general\nSubject to the availability of funds and in consultation with other relevant Federal agencies, amounts deposited in the Fund shall be available to the Secretary to provide grants for projects for the conservation of western monarch butterflies, and other pollinators within the range of western monarch butterflies, for which project proposals are approved by the Secretary in accordance with this section.\n##### (b) Project proposals\n**(1) Eligible entities**\nAn entity that is eligible to receive a grant for a project under this section is\u2014\n**(A)**\na relevant local government or Tribal government agency, research institution, or nonprofit organization with expertise required for the conservation of western monarch butterflies and other pollinators within the range of western monarch butterflies; and\n**(B)**\nany other entity, as determined appropriate by the Secretary, with the expertise required for the conservation of western monarch butterflies and other pollinators within the range of western monarch butterflies.\n**(2) Federal partnership opportunities**\nA State or Federal agency\u2014\n**(A)**\nmay not be a lead entity or receive a grant for a project under this section; but\n**(B)**\nmay be included as a partner or collaborator on a project that receives a grant under this section.\n**(3) Required elements**\nA proposal for a project under this section shall include\u2014\n**(A)**\na statement of the purposes of the project;\n**(B)**\nthe name of the entity with overall responsibility for the project;\n**(C)**\na description of\u2014\n**(i)**\nthe qualifications of the entity that will conduct the project;\n**(ii)**\nmethods for project implementation and outcome assessment; and\n**(iii)**\nanticipated outcomes;\n**(D)**\nassurances that the project will be implemented in consultation with relevant wildlife management authorities, Tribal governments, and other appropriate local government, State government, and Federal Government agencies;\n**(E)**\nassurances that the conservation efforts outlined in the proposal do not conflict with food safety measures or practices;\n**(F)**\ninformation that demonstrates the clear potential of the project to contribute to the conservation and recovery of western monarch butterflies and other pollinators within the range of western monarch butterflies; and\n**(G)**\nsuch other information as the Secretary may require.\n##### (c) Project review and approval\nThe Secretary shall annually\u2014\n**(1)**\nsolicit project proposals for funding under this section; and\n**(2)**\nreview each proposal described in paragraph (1) on a timeline that recognizes the urgency of the declining number of western monarch butterflies and other pollinators within the range of western monarch butterflies to determine whether the proposal meets the criteria described in subsection (d).\n##### (d) Criteria for approval\nThe Secretary may approve a project proposal under this section if the proposal demonstrates a likelihood that the project will contribute to the conservation of western monarch butterfly populations in the wild.\n##### (e) Technical assistance\nThe Secretary shall provide technical assistance for a project that receives a grant under this section.\n##### (f) Project reporting\n**(1) In general**\nEach entity that receives a grant for a project under this section shall submit to the Secretary, at such intervals as the Secretary may require, reports that include any information that the Secretary determines is necessary to evaluate the progress and success of the project for the purposes of ensuring positive results, assessing problems, and fostering improvements.\n**(2) Availability to State legislatures**\nAt the request of the Governor of the State in which a project is conducted, each entity that receives a grant for a project under this section shall submit each report under paragraph (1) to the State legislature of that State.\n**(3) Availability to the public**\nThe Secretary shall make available to the public, in a timely manner\u2014\n**(A)**\neach report submitted under paragraph (1); and\n**(B)**\nany other documents relating to projects for which a grant is provided under this section.\n#### 5. Western Monarch Butterfly Rescue Fund\n##### (a) Establishment\nThere is established in the Treasury of the United States a fund, to be known as the Western Monarch Butterfly Rescue Fund .\n##### (b) Administrative expenses\nOf the amounts available in the Fund for each fiscal year, the Secretary may expend not more than 3 percent to pay the administrative expenses necessary to carry out this Act.\n##### (c) Authorization of appropriations\nThere is authorized to be appropriated for deposit into the Fund $12,500,000 for each of fiscal years 2026 through 2030, to remain available until expended.\n#### 6. Implementation of the Western Monarch Butterfly Conservation Plan\n##### (a) In general\nThe Secretary shall enter into an agreement with the National Fish and Wildlife Foundation pursuant to the National Fish and Wildlife Foundation Establishment Act ( 16 U.S.C. 3701 et seq. ) to facilitate updating and implementing the Western Monarch Butterfly Conservation Plan prepared by the Western Association of Fish and Wildlife Agencies and dated January 2019.\n##### (b) Administration\nSection 10(a) of the National Fish and Wildlife Foundation Establishment Act ( 16 U.S.C. 3709(a) ) shall not apply with respect to\u2014\n**(1)**\nthe agreement entered into under subsection (a); or\n**(2)**\namounts made available to carry out this section.\n##### (c) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out this section $12,500,000 for each of fiscal years 2026 through 2030.\n#### 7. Report to Congress\nNot later than January 31 of each year, the Secretary shall submit to Congress a report describing the status of western monarch butterflies, including, with respect to the year for which the report is submitted\u2014\n**(1)**\na summary of the projects for which the Secretary has provided funding under section 4 and an evaluation of those projects; and\n**(2)**\na summary of the projects for which the Secretary has provided funding through the Western Monarch Butterfly Conservation Plan prepared by the Western Association of Fish and Wildlife Agencies and dated January 2019.",
      "versionDate": "2025-06-18",
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
        "actionDate": "2025-06-20",
        "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4062",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "MONARCH Act of 2025",
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
        "name": "Animals",
        "updateDate": "2025-07-14T14:27:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-18",
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
          "measure-id": "id119s2128",
          "measure-number": "2128",
          "measure-type": "s",
          "orig-publish-date": "2025-06-18",
          "originChamber": "SENATE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2128v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-06-18",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Monarch Action, Recovery, and Conservation of Habitat Act of 2025 or the MONARCH Act of 2025</strong></p><p>This bill provides support for the conservation of western monarch butterflies (the monarch butterfly population that overwinters along the coast of California and breeds across California, Arizona, Nevada, Washington, Oregon, Idaho, and Utah). Specifically, the bill establishes the Western Monarch Butterfly Rescue Fund. The Department of the Interior must use amounts in the fund to provide grants for the conservation of such butterflies and other pollinators within the range of western monarch butterflies.</p><p>In addition, Interior must enter into an agreement with the National Fish and Wildlife Foundation to facilitate updating and implementing the Western Monarch Butterfly Conservation Plan, which was prepared by the Western Association of Fish and Wildlife Agencies.</p>"
        },
        "title": "MONARCH Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2128.xml",
    "summary": {
      "actionDate": "2025-06-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Monarch Action, Recovery, and Conservation of Habitat Act of 2025 or the MONARCH Act of 2025</strong></p><p>This bill provides support for the conservation of western monarch butterflies (the monarch butterfly population that overwinters along the coast of California and breeds across California, Arizona, Nevada, Washington, Oregon, Idaho, and Utah). Specifically, the bill establishes the Western Monarch Butterfly Rescue Fund. The Department of the Interior must use amounts in the fund to provide grants for the conservation of such butterflies and other pollinators within the range of western monarch butterflies.</p><p>In addition, Interior must enter into an agreement with the National Fish and Wildlife Foundation to facilitate updating and implementing the Western Monarch Butterfly Conservation Plan, which was prepared by the Western Association of Fish and Wildlife Agencies.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s2128"
    },
    "title": "MONARCH Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Monarch Action, Recovery, and Conservation of Habitat Act of 2025 or the MONARCH Act of 2025</strong></p><p>This bill provides support for the conservation of western monarch butterflies (the monarch butterfly population that overwinters along the coast of California and breeds across California, Arizona, Nevada, Washington, Oregon, Idaho, and Utah). Specifically, the bill establishes the Western Monarch Butterfly Rescue Fund. The Department of the Interior must use amounts in the fund to provide grants for the conservation of such butterflies and other pollinators within the range of western monarch butterflies.</p><p>In addition, Interior must enter into an agreement with the National Fish and Wildlife Foundation to facilitate updating and implementing the Western Monarch Butterfly Conservation Plan, which was prepared by the Western Association of Fish and Wildlife Agencies.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s2128"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2128is.xml"
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
      "title": "MONARCH Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-02T01:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "MONARCH Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Monarch Action, Recovery, and Conservation of Habitat Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to encourage and facilitate efforts by States and other stakeholders to conserve and sustain the western population of monarch butterflies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-02T01:19:04Z"
    }
  ]
}
```
