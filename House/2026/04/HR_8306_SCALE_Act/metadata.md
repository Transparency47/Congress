# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8306?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8306
- Title: SCALE Act
- Congress: 119
- Bill type: HR
- Bill number: 8306
- Origin chamber: House
- Introduced date: 2026-04-15
- Update date: 2026-04-27T22:08:59Z
- Update date including text: 2026-04-27T22:08:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-15 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-04-15: Introduced in House

## Actions

- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-15 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-15",
    "latestAction": {
      "actionDate": "2026-04-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8306",
    "number": "8306",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001194",
        "district": "2",
        "firstName": "John",
        "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
        "lastName": "Moolenaar",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "SCALE Act",
    "type": "HR",
    "updateDate": "2026-04-27T22:08:59Z",
    "updateDateIncludingText": "2026-04-27T22:08:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Intelligence (Permanent Select) Committee",
          "systemCode": "hlig00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-15",
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
          "date": "2026-04-15T14:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Intelligence (Permanent Select) Committee",
      "systemCode": "hlig00",
      "type": "Select"
    },
    {
      "activities": {
        "item": {
          "date": "2026-04-15T14:03:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8306ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8306\nIN THE HOUSE OF REPRESENTATIVES\nApril 15, 2026 Mr. Moolenaar introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Permanent Select Committee on Intelligence , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Secretary of Commerce in coordination with the Director of National Intelligence to implement a process for establishing a rolling annual standard for the sale of certain integrated circuits to certain countries.\n#### 1. Short title\nThis Act may be cited as the Semiconductor Controls Adjusted to Limit Exports Act or the SCALE Act .\n#### 2. Statement of policy\nIt is the policy of the United States to\u2014\n**(1)**\nlead in global diffusion of artificial intelligence (AI) hardware and software;\n**(2)**\nshape international markets so that foreign adversaries remain reliant on United States and allied supply chains for AI hardware and software;\n**(3)**\npursue export promotion and export control agendas that enable the diffusion of United States AI hardware and software and enduring United States leadership in advanced artificial intelligence;\n**(4)**\nensure that the United States and its allies consistently apply export restrictions to ensure national security objectives and prevent backfill amongst allied and partner nations;\n**(5)**\nlimit the ability of adversaries to indigenize their own AI hardware production efforts, such limitation to include by crowding out their domestic markets with United States AI hardware;\n**(6)**\nprovide business stability in export controls through a systematic and repeatable process that annually assesses that indigenous capability of an entity of concern to produce AI hardware and set export control thresholds to an entity of concern based on that process; and\n**(7)**\nprevent any foreign adversary from accumulating, through any combination of indigenous production, import, or third-party access, a quantity of AI hardware that approaches parity with the aggregate AI hardware capacity of the United States.\n#### 3. Export promotion and control policy\n##### (a) Performance metrics\n**(1) Establishment**\nNot later than 180 days after the date of enactment of this Act, the Secretary and the Director, in coordination with other departments and agencies as necessary, shall establish and publicly release objective performance metrics that measure the state of AI hardware in entities of concern. The Secretary shall submit a classified annex to the appropriate congressional committees containing any information that the Secretary determines cannot be publicly released.\n**(2) Objectives**\nThe metrics shall assess\u2014\n**(A)**\nthe capability of individual AI hardware items indigenously produced by each entity of concern;\n**(B)**\nthe aggregate capability of all entities of concern to indigenously produce AI hardware items relative to the total demand for AI hardware of all entities of concern who purchase AI hardware; and\n**(C)**\nthe aggregate estimated amount of AI hardware located within all countries of concern or owned or controlled by an entity of concern.\n**(3) Inclusion of specific metrics**\nSuch metrics shall include, but are not limited to, individual chip capabilities, or where applicable aggregated, in the following categories:\n**(A)**\nTotal processing power.\n**(B)**\nInterconnect bandwidth.\n**(C)**\nMemory capacity bandwidth.\n##### (b) Assessment and report\n**(1) In general**\nNot later than 90 days after each update to the metrics established under subsection (a), the Secretary and the Director, in coordination with other departments and agencies as such Secretary and Director determine necessary, shall submit a report to the appropriate congressional committees assessing the quantity and quality of AI hardware produced in each country of concern using such metrics.\n**(2) Contents**\nThe assessment required under paragraph (1) shall include\u2014\n**(A)**\nfor each metric, the aggregate estimated amount of AI hardware, broken down by quarter, installed in each country of concern, delineated by AI hardware produced by AI hardware designers that are an entity of concern and AI hardware produced outside of a country of concern and imported into a country of concern;\n**(B)**\nfor each metric, the aggregate estimated amount of AI hardware installed outside of a country of concern and owned or controlled by any entity of concern;\n**(C)**\nfor each metric, the aggregate estimated amount of AI hardware\u2014\n**(i)**\nlegally available to an entity of concern through remote access;\n**(ii)**\ninstalled outside of a country of concern; and\n**(iii)**\nnot owned or controlled by an entity of concern;\n**(D)**\na breakdown of subparagraph (B) in terms of the country of origin of the AI hardware designer (with respect to this subparagraph, the country of origin of a unit of AI hardware shall be considered to be the country in which the designer of that unit of AI hardware is domiciled);\n**(E)**\nfor each metric, the combined total of the hardware identified in subparagraphs (A), (B), and (C), expressed as a percentage of the aggregate amount of AI hardware physically present in and intended for use within the United States;\n**(F)**\na breakdown by country of origin of the aggregate amount of AI hardware physically present in and intended for use within the United States. For this purpose, the country of origin of a unit of AI hardware shall be considered to be the country in which the designer of that unit of AI hardware is domiciled; and\n**(G)**\na technical assessment of the capability of the most advanced AI hardware designed by an entity of concern as compared to the state-of-the-art for that hardware.\n##### (c) AI export control threshold\nThe Secretary shall adopt an export control policy for AI hardware, including such a policy for remote access of such hardware, to any entity of concern in accordance with the following:\n**(1)**\nNot later than 365 days after the date of enactment of this Act, and not less than annually thereafter, use the findings from the assessment in subsection (b), to set an upper limit for the export of AI hardware to an entity of concern expressed in terms of the metrics developed in subsection (a) as follows:\n**(A)**\nThe upper limit shall be implemented as a policy of denial for license applications to export, reexport, transfer (in-country), or provide remote access to AI hardware.\n**(B)**\nThe upper limit for any individual item of AI hardware shall be set at a level not to exceed 110 percent of the performance, as measured by the metrics developed under subsection (a), of the most capable AI hardware item that meets the indigenous production threshold established under subparagraph (C).\n**(C)**\nAn individual item of AI hardware produced by an entity of concern shall be considered in establishing the upper limit under subparagraph (B) only if such item is manufactured in sustained serial production at a volume sufficient to fulfill not less than 25 percent of the estimated annual aggregate demand for AI hardware among all entities of concern, as assessed by the Secretary using the most recent assessment under subsection (b). AI hardware produced solely in experimental, prototype, or limited demonstration quantities shall not be considered for purposes of establishing the upper limit.\n**(D)**\nIf, at the time of any assessment under subsection (b), no individual item of AI hardware produced by an entity of concern meets the production threshold established under subparagraph (C), then applications for the export of or provision of remote access to AI hardware to any entity of concern shall be reviewed under a policy of denial.\n**(E)**\nIn no case shall the upper limit established under this paragraph be lower than the upper limit in effect during the preceding assessment period, unless the Secretary provides a written determination to the appropriate congressional committees that a reduction is necessary to address a specific and identified national security threat.\n**(2)**\nFor each metric established under subsection (a), the Secretary shall require a license for any export, reexport, transfer (in-country), or provide remote access to, AI hardware to any entity of concern, and shall review licenses under a presumption of denial if the approval of such license would cause the aggregate estimated amount of adversary AI hardware to exceed, in the aggregate, 5 percent of the aggregate estimated amount of AI hardware physically present in and intended for use within the United States.\n##### (d) Authority To update metrics\nOn and after the date that is 24 months after the date on which the first assessment under subsection (b) is submitted, the Secretary may add, modify, or remove the metrics established under subsection (a), subject to the following:\n**(1)**\nThe Secretary shall provide written notice to the appropriate congressional committees not less than 90 days before any such addition, modification, or removal takes effect, including a detailed justification for each proposed change and an assessment of how such change would affect the export control thresholds established under subsection (d).\n**(2)**\nNo modification or removal of a metric under this subsection shall take effect if, within the 90-day notice period under paragraph (1), either the Committee on Foreign Affairs of the House of Representatives or the Committee on Banking, Housing, and Urban Affairs of the Senate submits to the Secretary a written objection stating that the proposed change would undermine the purposes of this Act.\n##### (e) Conditions for license review on other than a presumption of denial basis\nAny license application to export AI hardware to any entity of concern reviewed under the upper limit established under subsection (d)(1) on other than a presumption of denial basis shall include certification by the applicant that\u2014\n**(1)**\nthe license will not result in any delay in fulfilling existing or new orders from customers in the United States for end use in the United States for any advanced-node integrated circuits produced by the applicant, taking into account normal lead times, and that global foundry capacity that would otherwise be used to produce similar or more advanced integrated circuits for end users in the United States will not be diverted to produce items authorized by the license;\n**(2)**\nfor the AI hardware described in the license application, the aggregate total processing performance of such hardware exported to any entity of concern does not exceed 50 percent of the aggregate total processing performance of the same hardware shipped to customers in the United States for end use in the United States;\n**(3)**\nthe items are not destined for military end use, military-intelligence end use, or weapons of mass destruction end use, and that the ultimate consignee will employ know-your-customer procedures to screen and prevent unauthorized remote access by prohibited parties;\n**(4)**\nprior to export, every shipment of AI hardware described in the license application will be reviewed by a qualified independent third-party testing laboratory headquartered in the United States, not under the control of any entity of concern, and having no financial interest in any party to the transaction, to confirm that the technical capabilities of the items are consistent with the representations in the license application; and\n**(5)**\nif the ultimate consignee or end user provides infrastructure-as-a-service, the consignee or end user will not transfer model weights trained on the exported AI hardware to any end user not disclosed in the license application, and will not provide any prohibited party with remote access to any model trained on such hardware.\n#### 4. Rules of construction\nNothing in this Act may be construed to direct the Secretary to\u2014\n**(1)**\ndecontrol or reduce export control thresholds based on assessment findings; or\n**(2)**\napprove licenses for sales of AI hardware or software.\n#### 5. Definitions\nIn this Act:\n**(1) AI hardware**\nThe term AI hardware means\u2014\n**(A)**\nany integrated circuit, computer, electronic assembly, or other item classified under Export Control Classification Numbers 3A090, 4A090, or any related Export Control Classification Number designated with a .z suffix under the Commerce Control List (supplement number 1 to part 774 of title 15, Code of Federal Regulations (or a successor regulation)); and\n**(B)**\nany other item designated by the Secretary, by regulation, as AI hardware for the purposes of this Act.\n**(2) Aggregate estimated amount of AI hardware**\nThe term aggregate estimated amount of AI hardware means the total quantity of AI hardware, as measured using the metrics established by the Secretary under section 3(a).\n**(3) Aggregate estimated amount of adversary AI hardware**\nThe term aggregate estimated amount of adversary AI hardware means the aggregate estimated amount of AI hardware\u2014\n**(A)**\ninstalled across all countries of concern; or\n**(B)**\naccessible to any entity of concern, including through remote access to AI hardware installed outside of any country of concern.\n**(4) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs of the House of Representatives;\n**(B)**\nthe Permanent Select Committee on Intelligence of the House of Representatives;\n**(C)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate; and\n**(D)**\nthe Select Committee on Intelligence of the Senate.\n**(5) Country of concern**\nThe term country of concern means\u2014\n**(A)**\nthe People\u2019s Republic of China, including the Hong Kong and Macau Special Administrative Regions;\n**(B)**\nthe Republic of Cuba;\n**(C)**\nthe Islamic Republic of Iran;\n**(D)**\nthe Democratic People\u2019s Republic of Korea;\n**(E)**\nthe Russian Federation; and\n**(F)**\nany other foreign country\u2014\n**(i)**\nlisted in the Country Group D:5 under Supplement No. 1 to part 740 of the Export Administration Regulations, as published on January 1, 2026;\n**(ii)**\ndesignated by the Secretary of State as a country of concern for purposes of this section; and\n**(iii)**\nnotice of such designation has been published in the Federal Register.\n**(6) Director**\nThe term Director means the Director of National Intelligence.\n**(7) Entity of concern**\nThe term entity of concern means any entity\u2014\n**(A)**\norganized under the laws of any country of concern;\n**(B)**\nhaving its principal place of business in any country of concern;\n**(C)**\nof which more than 10 percent of the ultimate beneficial ownership is held, directly or indirectly, by one or more persons or entities that are organized under the laws of, have their principal place of business in, or are nationals of any country of concern; or\n**(D)**\nthat is owned or controlled by, or acts on behalf of, the government of any country of concern.\n**(8) Indigenous production**\nThe term indigenous production , with respect to AI hardware\u2014\n**(A)**\nmeans AI hardware that is\u2014\n**(i)**\nphysically fabricated within the territory of the People\u2019s Republic of China; and\n**(ii)**\ndesigned by any entity of concern; and\n**(B)**\nexcludes AI hardware that is designed by any entity of concern but fabricated outside of any country of concern for purposes of this Act.\n**(9) Remote access**\nThe term remote access means access on a purposeful, knowing, reckless, or negligent basis to an item subject to the jurisdiction of the United States under this Act by a foreign person through a network connection, including the internet or a cloud computing service, from a location other than where the item is physically located if the Secretary determines that the use of the item could pose a serious risk to the national security or foreign policy of the United States.\n**(10) Secretary**\nThe term Secretary means the Secretary of Commerce.",
      "versionDate": "2026-04-15",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-04-27T22:08:59Z"
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
      "date": "2026-04-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8306ih.xml"
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
      "title": "SCALE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T06:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SCALE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-21T06:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Semiconductor Controls Adjusted to Limit Exports Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-21T06:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Commerce in coordination with the Director of National Intelligence to implement a process for establishing a rolling annual standard for the sale of certain integrated circuits to certain countries.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-21T06:03:38Z"
    }
  ]
}
```
