# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2652?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2652
- Title: Pacific Ready Coast Guard Act
- Congress: 119
- Bill type: S
- Bill number: 2652
- Origin chamber: Senate
- Introduced date: 2025-08-01
- Update date: 2025-09-19T18:42:59Z
- Update date including text: 2025-09-19T18:42:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in Senate
- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-08-01: Introduced in Senate

## Actions

- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2652",
    "number": "2652",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001194",
        "district": "",
        "firstName": "Brian",
        "fullName": "Sen. Schatz, Brian [D-HI]",
        "lastName": "Schatz",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Pacific Ready Coast Guard Act",
    "type": "S",
    "updateDate": "2025-09-19T18:42:59Z",
    "updateDateIncludingText": "2025-09-19T18:42:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-01",
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
      "actionDate": "2025-08-01",
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
          "date": "2025-08-01T19:47:03Z",
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
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "MS"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "HI"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2652is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2652\nIN THE SENATE OF THE UNITED STATES\nAugust 1, 2025 Mr. Schatz (for himself, Mr. Wicker , Ms. Hirono , and Ms. Duckworth ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend title 14, United States Code, to require an annual plan and budget display for Coast Guard operations in the Pacific, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pacific Ready Coast Guard Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation, the Committee on Appropriations, the Committee on Armed Services, and the Committee on Foreign Relations of the Senate; and\n**(B)**\nthe Committee on Transportation and Infrastructure, the Committee on Appropriations, the Committee on Armed Services, and the Committee on Foreign Affairs of the House of Representatives.\n**(2) Commandant**\nThe term Commandant means the Commandant of the Coast Guard.\n#### 3. Annual plan and budget display for Coast Guard operations in the Pacific\n##### (a) In general\nChapter 51 of title 14, United States Code, is amended by adding at the end the following:\n5116. Annual plan for Coast Guard operations in the Pacific (a) In general Not later than December 31, 2025, and annually thereafter, the Commandant, in consultation with the Secretary of State and the Secretary of Defense, shall submit to the appropriate committees of Congress a plan for Coast Guard operations in the Pacific region for the year after the year during which the plan is submitted. Such plan shall include, for the year covered by the plan, each of the following: (1) A list of objectives for Coast Guard engagement in the Pacific region in support of Department of State and Department of Defense missions. (2) An assessment of the capabilities of the Coast Guard to support Department of State and Department of Defense missions in the Pacific region. (3) A list of any areas in the Pacific region in which an increased Coast Guard presence would better support Department of State and Department of Defense missions. (4) The projected demand for Coast Guard engagement in the Pacific region from the Department of State and the Department of Defense for the year covered by the plan and during the subsequent 10-year period. (5) An assessment of whether the Coast Guard will be able to meet such projected demand for the year covered by the plan, including a list of any factors limiting the ability of the Coast Guard to meet such projected demand. (6) A summary of the resources needed for the Coast Guard to meet such projected demand for the year covered by the plan, including\u2014 (A) staff; (B) infrastructure, including shore infrastructure; (C) administrative and logistical support; and (D) technology. (7) Any other matter the Commandant considers appropriate. (b) Form Each plan required by subsection (a) shall be submitted in unclassified form but may include a classified annex. (c) Briefing required Not later than February 15, 2026, and annually thereafter, the Commandant shall provide to the appropriate committees of Congress a briefing on the annual plan required by subsection (a) submitted during the preceding year. (d) Appropriate committees of Congress defined In this section, the term appropriate committees of Congress means\u2014 (1) the Committee on Commerce, Science, and Transportation, the Committee on Appropriations, and the Committee on Armed Services of the Senate; and (2) the Committee on Transportation and Infrastructure, the Committee on Appropriations, and the Committee on Armed Services of the House of Representatives. 5117. Annual budget display for Coast Guard operations in the Pacific (a) In general Not later than February 15, 2026, and annually thereafter, the Commandant shall submit to the appropriate committees of Congress a detailed budget display for Coast Guard operations in the Pacific region for the fiscal year after the fiscal year during which the budget display is submitted. The Commandant shall base such budget display on the projected demand for Coast Guard engagement in the Pacific region as identified in the most recent annual plan developed under section 5116 of this title. Such budget display shall include, for the year covered by the budget display, the following information: (1) With respect to procurement accounts, amounts displayed by account, budget activity, line number, line item, and line item title. (2) With respect to research, development, test, and evaluation accounts, amounts displayed by account, budget activity, line number, program element, and program element title. (3) With respect to operation and maintenance accounts, amounts displayed by account title, budget activity title, line number, and subactivity group title. (4) With respect to military personnel accounts, amounts displayed by account, budget activity, budget subactivity, and budget subactivity title. (b) Form Each display under subsection (a) shall be submitted in unclassified form, but may include a classified annex. (c) Briefing required Not later than February 15, 2026, and annually thereafter, the Commandant shall provide to the appropriate congressional committees a briefing on the budget display required by subsection (a) for the fiscal year after the fiscal year during which the briefing is provided. (d) Appropriate committees of Congress defined In this section, the term appropriate committees of Congress means\u2014 (1) the Committee on Commerce, Science, and Transportation, the Committee on Appropriations, and the Committee on Armed Services of the Senate; and (2) the Committee on Transportation and Infrastructure, the Committee on Appropriations, and the Committee on Armed Services of the House of Representatives. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of chapter 51 of title 14, United States Code, is amended by adding at the end the following new items:\n5116. Annual plan for the Coast Guard operations in the Pacific.\n5117. Annual budget display for Coast Guard operations in the Pacific.\n#### 4. Report on feasibility of standing Indo-Pacific maritime group\n##### (a) In general\nNot later than 120 days after the date of the enactment of this Act, the Commandant shall submit to the appropriate committees of Congress a report on the feasibility of establishing a standing Indo-Pacific maritime group, modeled after the standing North Atlantic Treaty Organization maritime groups, to conduct humanitarian and law enforcement missions in the Indo-Pacific region.\n##### (b) Elements\nThe report required by subsection (a) shall include the following:\n**(1)**\nFindings on the manner in which a standing Indo-Pacific maritime group could enable the Coast Guard to work more effectively with partner countries in the Indo-Pacific region on\u2014\n**(A)**\nmultilateral humanitarian missions;\n**(B)**\nanti-piracy missions;\n**(C)**\nemergency responses;\n**(D)**\nmaritime domain awareness issues; and\n**(E)**\nthe prevention of unregulated and unreported fishing efforts.\n**(2)**\nAny other matter the Commandant considers appropriate.\n#### 5. Report on establishment of forward operating bases\n##### (a) In general\nNot later than 1 year after the date of the enactment of this Act, the Commandant, in consultation with the Commander of the United States Indo-Pacific Command, shall submit to the appropriate committees of Congress a report on establishing forward operating bases in the Indo-Pacific region.\n##### (b) Elements\nThe report required by subsection (a) shall include the following:\n**(1)**\nA description of gaps in Coast Guard operations in the Indo-Pacific region, including any logistical problems.\n**(2)**\nA list of locations selected for the establishment of forward operating bases in the Indo-Pacific region, including mobile forward operating bases.\n**(3)**\nA justification for the selection of each location on such list.\n**(4)**\nThe cost of establishing such forward operating bases.\n**(5)**\nThe non-monetary resources and approvals needed to establish such forward operating bases, including authorizations and cooperation agreements.\n**(6)**\nA timeline for completing, not later than January 1, 2030, the establishment of such forward operating bases.\n#### 6. Report on Coast Guard attach\u00e9s\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Commandant, in consultation with the Secretary of State, shall submit to the appropriate committees of Congress a report on Coast Guard attach\u00e9s serving in embassies in the Indo-Pacific region.\n##### (b) Elements\nThe report required by subsection (a) shall include the following:\n**(1)**\nThe number of such Coast Guard attach\u00e9s actively serving in embassies in the Indo-Pacific region.\n**(2)**\nA list of such embassies at which an increased allocation of such attach\u00e9s could better support United States objectives in the Indo-Pacific region.\n**(3)**\nA plan to increase the number of such attach\u00e9s actively serving in such embassies, including the resources and approvals necessary to achieve such plan.\n#### 7. Report on Department of State consular officers joining Coast Guard and Navy missions to Pacific Island countries\n##### (a) In general\nNot later than 120 days after the date of the enactment of this Act, the Secretary of Defense, in coordination with the Commandant, the Commander of the United States Indo-Pacific Command, and the Chief of Naval Operations, shall submit to the appropriate committees of Congress a report that analyzes the feasibility of an initiative to attach Department of State consular officers to Coast Guard and Navy missions in Pacific Island countries.\n##### (b) Elements\nThe report required by subsection (a) shall include the following:\n**(1)**\nAn assessment of the current demand for consular services from citizens of Pacific Island countries and the challenges such citizens face in obtaining consular services.\n**(2)**\nAn assessment of the approximate time and resources citizens of Pacific Island countries that do not host United States embassies would save by having their United States visas adjudicated, or by receiving other consular services, through the initiative described in subsection (a).\n**(3)**\nAn assessment of the cost that would be incurred by the Department of State, the Coast Guard, the United States Indo-Pacific Command, and the Navy through the implementation of such initiative, including potential alternative cost-effective options and recommendations for providing efficient consular services to Pacific Island countries.\n**(4)**\nAn assessment of the frequency and duration of Coast Guard and Navy deployments to Pacific Island countries, including\u2014\n**(A)**\ndeployment frequency measured against the desired number of visits;\n**(B)**\nthe amount of time typically spent in port for such visits; and\n**(C)**\ndisruption to planned Coast Guard and Navy missions in order to visit locations needing consular assistance.\n**(5)**\nAn evaluation of the logistical issues needing to be addressed to implement the initiative, including\u2014\n**(A)**\nan analysis of spacing requirements to host Department of State personnel and equipment aboard Coast Guard and Navy vessels;\n**(B)**\nan analysis of the information technology and connectivity requirements to conduct consular affairs activities;\n**(C)**\nthe feasibility of printing visas aboard Coast Guard and Navy vessels or alternatives to such printing, including remote printing and mailing of passports with visas;\n**(D)**\nthe maintenance of the physical security of consular officers and relevant adjudication equipment, including computer systems and visa foils, during such missions;\n**(E)**\nthe impacts on the operations and security of Coast Guard and Navy vessels; and\n**(F)**\nthe estimated time consular officers would spend on board Coast Guard and Navy vessels between visits to Pacific Island countries.",
      "versionDate": "2025-08-01",
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
        "updateDate": "2025-09-19T18:42:59Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2652is.xml"
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
      "title": "Pacific Ready Coast Guard Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-13T03:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Pacific Ready Coast Guard Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 14, United States Code, to require an annual plan and budget display for Coast Guard operations in the Pacific, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T03:03:18Z"
    }
  ]
}
```
