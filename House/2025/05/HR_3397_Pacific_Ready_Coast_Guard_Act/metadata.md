# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3397?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3397
- Title: Pacific Ready Coast Guard Act
- Congress: 119
- Bill type: HR
- Bill number: 3397
- Origin chamber: House
- Introduced date: 2025-05-14
- Update date: 2025-06-12T08:06:11Z
- Update date including text: 2025-06-12T08:06:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-17 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- Latest action: 2025-05-14: Introduced in House

## Actions

- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-17 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3397",
    "number": "3397",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "K000388",
        "district": "1",
        "firstName": "Trent",
        "fullName": "Rep. Kelly, Trent [R-MS-1]",
        "lastName": "Kelly",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Pacific Ready Coast Guard Act",
    "type": "HR",
    "updateDate": "2025-06-12T08:06:11Z",
    "updateDateIncludingText": "2025-06-12T08:06:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-17",
      "committees": {
        "item": {
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Coast Guard and Maritime Transportation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-14",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-14",
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
          "date": "2025-05-14T14:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-17T21:01:55Z",
              "name": "Referred to"
            }
          },
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "HI"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "AS"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "GU"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "CA"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "FL"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "IL"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "MP"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3397ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3397\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2025 Mr. Kelly of Mississippi (for himself and Mr. Case ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 14, United States Code, to require the establishment of the Center of Expertise in Indo-Pacific Maritime Governance, and for other purposes.\n#### 1. Short Title\nThis Act may be cited as the Pacific Ready Coast Guard Act .\n#### 2. Center of Expertise in Indo-Pacific Maritime Governance\n##### (a) In general\nChapter 3 of title 14, United States Code, is amended by adding at the end the following new section:\n324. Center of Expertise in Indo-Pacific Maritime Governance (a) Establishment The Commandant of the Coast Guard shall establish a Center of Expertise in Indo-Pacific Maritime Governance (in this section referred to as the Center ). The Commandant shall model the Center after the International Law Enforcement Academies and the Department of Defense Institutes. (b) Mission The Center shall be used to provide and facilitate education, training, and research in maritime governance best practices, including how to build regional state capacity. (c) Assistance To assist the Center in carrying out the mission under subsection (b), upon request of the Center, the head of any Federal agency may grant to the Center access to the data, archives, and other resources of that agency, and may detail any personnel of that agency to the Center. (d) Joint operation with partner country The Commandant shall seek to engage with appropriate representatives of a foreign country selected at the discretion of the Commandant to reach an agreement for the operation of the Center. Any such agreement shall provide for such country to furnish necessary administrative services and facilities for the Center, including by\u2014 (1) directly providing such services; (2) providing the funds for such services; or (3) coordinating with officials of an institution of higher education located in such foreign country for the provision of such services. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by adding at the end the following new item:\n324. Center of Expertise in Indo-Pacific Maritime Governance. .\n#### 3. Annual plan for Coast Guard operations in the Pacific\n##### (a) In general\nChapter 51 of title 14, United States Code, is amended by adding at the end the following new sections:\n5116. Annual plan for Coast Guard operations in the Pacific (a) In general Not later than December 31, 2025, and annually thereafter, the Commandant of the Coast Guard, in consultation with the Secretary of State and Secretary of Defense, shall submit to the appropriate congressional committees a plan for Coast Guard operations in the Pacific region for the year after the year during which the plan is submitted. Such plan shall include, for the year covered by the plan, each of the following elements: (1) A list of objectives for Coast Guard engagement in the Pacific region in support of Department of State and Department of Defense missions. (2) An assessment of the capabilities of the Coast Guard to support Department of State and Department of Defense missions in the Pacific region. (3) A list of any areas in the Pacific region where an increased Coast Guard presence would better support Department of State and Department of Defense missions. (4) The projected demand for Coast Guard engagement in the Pacific region from the Department of State and the Department of Defense for the year covered by the plan and the subsequent 10 years. (5) An assessment of whether the Coast Guard will be able to meet such projected demand for the year covered by the plan, including a list of any factors limiting the ability of the Coast Guard to meet such projected demand. (6) A summary of the resources needed for the Coast Guard to meet such projected demand for the year covered by the plan, including\u2014 (A) staff; (B) infrastructure, including shore infrastructure; (C) administrative and logistical support; and (D) technology. (7) Any other matter as determined relevant by the Commandant. (b) Form Each plan under subsection (a) shall be submitted in unclassified form, but may include a classified annex. (c) Briefing required Not later than February 15, 2026, and annually thereafter, the Commandant shall provide to the appropriate congressional committees a briefing on the annual plan required under subsection (a) submitted during the preceding year. (d) Appropriate congressional committees defined In this section, the term appropriate congressional committees means\u2014 (1) the Committee on Transportation and Infrastructure of the House of Representatives; (2) the Committee on Appropriations of the House of Representatives; (3) the Committee on Armed Services of the House of Representatives; (4) the Committee on Commerce, Science, and Transportation of the Senate; (5) the Committee on Appropriations of the Senate; and (6) the Committee on Armed Services of the Senate. 5117. Annual budget display for Coast Guard operations in the Pacific (a) In general Not later than February 15, 2026, and annually thereafter, the Commandant of the Coast Guard shall submit to the appropriate congressional committees a detailed budget display for Coast Guard operations in the Pacific region for the fiscal year after the fiscal year during which the budget display is submitted. The Commandant shall base such budget display on the projected demand for Coast Guard engagement in the Pacific region as identified in the most recent annual plan developed under section 5116 of this title. Such budget display shall include, for the year covered by the budget display, the following information: (1) With respect to procurement accounts, amounts displayed by account, budget activity, line number, line item, and line item title. (2) With respect to research, development, test, and evaluation accounts, amounts displayed by account, budget activity, line number, program element, and program element title. (3) With respect to operation and maintenance accounts, amounts displayed by account title, budget activity title, line number, and subactivity group title. (4) With respect to military personnel accounts, amounts displayed by account, budget activity, budget subactivity, and budget subactivity title. (b) Form Each display under subsection (a) shall be submitted in unclassified form, but may include a classified annex. (c) Briefing required Not later than February 15, 2026, and annually thereafter, the Commandant shall provide to the appropriate congressional committees a briefing on the budget display required by subsection (a) for the fiscal year after the fiscal year during which the briefing is provided. (d) Appropriate congressional committees defined In this section, the term appropriate congressional committees has the meaning given such term in section 5116 of this title. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by adding at the end the following new items:\n5116. Annual plan for Coast Guard operations in the Pacific. 5117. Annual budget display for Coast Guard operations in the Pacific. .\n#### 4. Report on feasibility of standing Indo-Pacific maritime group\n##### (a) In general\nNot later than 120 days after the date of the enactment of this Act, the Commandant of the Coast Guard shall submit to the appropriate congressional committees a report on the feasibility of establishing a standing Indo-Pacific maritime group, modeled after the Standing NATO Maritime Groups, to conduct humanitarian and law enforcement missions in the Indo-Pacific region.\n##### (b) Contents\nThe Commandant shall include in the report required under subsection (a)\u2014\n**(1)**\nfindings on how such maritime group could enable the Coast Guard to work more effectively with partner countries in the Indo-Pacific region on\u2014\n**(A)**\nmultilateral humanitarian missions;\n**(B)**\nanti-piracy missions;\n**(C)**\nemergency responses;\n**(D)**\nmaritime domain awareness issues; and\n**(E)**\nthe prevention of unregulated and unreported fishing efforts; and\n**(2)**\nany other matters as determined relevant by the Commandant.\n#### 5. Report on establishment of forward operating bases\n##### (a) In general\nNot later than 1 year after the date of the enactment of this Act, the Commandant of the Coast Guard, in consultation with the Commander of the United States Indo-Pacific Command, shall submit to the appropriate congressional committees a report on establishing forward operating bases in the Indo-Pacific region.\n##### (b) Contents\nThe Commandant shall include in the report required under subsection (a)\u2014\n**(1)**\na description of gaps in Coast Guard operations in the Indo-Pacific region, including any logistical problems;\n**(2)**\na list of locations selected for the establishment of such forward operating bases, including mobile forward operating bases;\n**(3)**\na description of why each location on such list was selected;\n**(4)**\nthe cost of establishing such forward operating bases;\n**(5)**\nthe non-monetary resources and approvals needed to establish such forward operating bases, including authorizations and cooperation agreements; and\n**(6)**\na timeline for completing by not later than January 1, 2030, the establishment of such forward operating bases.\n#### 6. Report on Coast Guard attach\u00e9s\n##### (a) In general\nNot later than 6 months after the date of the enactment of this Act, the Commandant of the Coast Guard, in consultation with the Secretary of State, shall submit to the appropriate congressional committees a report on Coast Guard attach\u00e9s serving in embassies in the Indo-Pacific region.\n##### (b) Contents\nThe Commandant shall include in the report required under subsection (a)\u2014\n**(1)**\nthe number of such attach\u00e9s actively serving in such embassies;\n**(2)**\na list of any such embassies where an increased allocation of such attach\u00e9s could better support United States objectives in the Indo-Pacific region; and\n**(3)**\na plan to increase the number of such attach\u00e9s actively serving in such embassies, including the resources and approvals necessary to achieve such plan.\n#### 7. Appropriate congressional committees defined\nIn this Act, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Transportation and Infrastructure of the House of Representatives;\n**(2)**\nthe Committee on Appropriations of the House of Representatives;\n**(3)**\nthe Committee on Armed Services of the House of Representatives;\n**(4)**\nthe Committee on Commerce, Science, and Transportation of the Senate;\n**(5)**\nthe Committee on Appropriations of the Senate; and\n**(6)**\nthe Committee on Armed Services of the Senate.",
      "versionDate": "2025-05-14",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-06-10T15:09:50Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3397ih.xml"
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
      "title": "Pacific Ready Coast Guard Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T03:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pacific Ready Coast Guard Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 14, United States Code, to require the establishment of the Center of Expertise in Indo-Pacific Maritime Governance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T03:48:24Z"
    }
  ]
}
```
