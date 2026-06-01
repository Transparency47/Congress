# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8575?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8575
- Title: EMPOWER Act
- Congress: 119
- Bill type: HR
- Bill number: 8575
- Origin chamber: House
- Introduced date: 2026-04-29
- Update date: 2026-05-12T19:53:53Z
- Update date including text: 2026-05-12T19:53:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-29: Introduced in House
- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2026-04-29: Introduced in House

## Actions

- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8575",
    "number": "8575",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "J000310",
        "district": "32",
        "firstName": "Julie",
        "fullName": "Rep. Johnson, Julie [D-TX-32]",
        "lastName": "Johnson",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "EMPOWER Act",
    "type": "HR",
    "updateDate": "2026-05-12T19:53:53Z",
    "updateDateIncludingText": "2026-05-12T19:53:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-29",
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
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-29",
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
          "date": "2026-04-29T13:03:40Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8575ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8575\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2026 Ms. Johnson of Texas introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo strengthen the public-private partnerships and policy efforts of the Department of State to advance women\u2019s economic security in South and Central Asia, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Enhancing Mobilization of Public-Private Organizations for Women\u2019s Economic Rights Act or the EMPOWER Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nWomen\u2019s full and unfettered political, economic, and social participation is vital to realizing universal human rights, global prosperity, peace, and security.\n**(2)**\nWomen\u2019s labor force participation, asset ownership, and economic security are development multipliers, promoting family financial resilience, community health and development, children\u2019s educational attainment, and poverty reduction, among other development gains across South and Central Asia.\n**(3)**\nWomen\u2019s economic participation and opportunity, educational attainment, health and survival, and political empowerment are directly proportional to countries\u2019 economic competitiveness.\n**(4)**\nWomen make up about 33 percent of South Asia\u2019s labor force, among the lowest female labor force participation rates in the world, yet gender parity in employment could increase South Asia\u2019s Gross Domestic Product by between 19 to 58 percent.\n**(5)**\nWhile the percentage varies across the five Central Asian states, Tajikistan and Uzbekistan also have some of the lowest female labor force participation rates in the world, at 29.6 percent and 35.9 percent, respectively.\n**(6)**\nThe Women\u2019s Councils are consortia of public-private partnerships between the Department of State and United States and South Asian businesses, civil society, and universities, to matchmake technology, networks, expertise, and resources of our corporate and civil society members to create more impact together than any entity could alone.\n**(7)**\nThe Women\u2019s Councils implement President Trump\u2019s Presidential Memorandum on Promoting Women\u2019s Global Development and Prosperity and the bipartisan Women, Peace, and Security Act of 2017.\n**(8)**\nThe Women\u2019s Councils accelerate women\u2019s economic empowerment in South and Central Asian countries, growing economies and advancing stability and prosperity for all, at no cost to American taxpayers.\n#### 3. Statement of policy\nIt is the policy of the United States to promote women\u2019s economic security and advancement, including in South and Central Asia, as an integral part of the broader conduct of United States foreign policy in the region.\n#### 4. Women\u2019s councils and public-private partnerships advancing women\u2019s economic security in South and Central Asia\n##### (a) In general\nThe Secretary of State shall maintain and seek to expand existing women\u2019s councils and other public-private partnerships that\u2014\n**(1)**\nforge ties between the United States and countries in South and Central Asia, by catalyzing commitments from the private sector, civil society, and academia; and\n**(2)**\nadvance women\u2019s employment, entrepreneurship and access to education, such as the United States-Pakistan Women\u2019s Council, the United States-India Alliance for Women\u2019s Economic Empowerment, and the Alliance for Afghan Women\u2019s Economic Resilience.\n##### (b) Sense of Congress\nIt is the sense of Congress that the activities authorized under subsection (a) should support\u2014\n**(1)**\nwomen\u2019s financial inclusion and access;\n**(2)**\nwomen\u2019s access to mentorship;\n**(3)**\nwomen\u2019s asset ownership;\n**(4)**\nincubation and scaling of women-owned startups and small and medium enterprises;\n**(5)**\naccess to procurement opportunities by women entrepreneurs;\n**(6)**\ncareer-enhancing educational opportunities;\n**(7)**\nwomen in science, technology, engineering, the arts and mathematics;\n**(8)**\nthe care economy; and\n**(9)**\naddressing legal and social barriers to women\u2019s economic empowerment.\n##### (c) Location\nActivities authorized under this section may be conducted in the United States, in countries in South and Central Asia, or in third countries.\n#### 5. Establishment of Unit\n##### (a) In general\nThe Secretary of State shall establish within the Bureau of South and Central Asian Affairs a Unit responsible for overseeing the public-private partnerships described in section 4(a). Such Unit shall be led by a Special Advisor for Women\u2019s Economic Security, who shall report to the Assistant Secretary of State for South and Central Asia.\n##### (b) Special advisor\nThe Special Advisor for Women\u2019s Economic Security shall\u2014\n**(1)**\nbe appointed by the Secretary of State, including from among existing officials or employees of the Department of State to serve as the Special Advisor in addition to that official or employee\u2019s existing role; and\n**(2)**\nhave the rank and status of Ambassador.\n##### (c) Designated point of contact\nEach United States diplomatic and consular post the Special Advisor determines relevant shall designate a point of contact from among the personnel of such post, whose duties shall include identifying and tracking relevant private sector commitments with respect to the public-private partnerships overseen by the Unit established under subsection (a).\n#### 6. Report\n##### (a) In general\nNot later than 1 year after the date of the enactment of this Act, the Secretary of State shall submit to the appropriate congressional committees a report that includes\u2014\n**(1)**\na description of the steps taken to implement this Act, including allocated personnel and funding;\n**(2)**\nthe status of the commitments and partnerships described in section 4(a); and\n**(3)**\neconomic data on the impact of work of the Unit authorized by section 5.\n##### (b) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means the following:\n**(1)**\nThe Committee on Foreign Affairs of the House of Representatives.\n**(2)**\nThe Committee on Foreign Relations of the Senate.",
      "versionDate": "2026-04-29",
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
        "name": "International Affairs",
        "updateDate": "2026-05-12T19:53:53Z"
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
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8575ih.xml"
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
      "title": "EMPOWER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T09:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "EMPOWER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Enhancing Mobilization of Public-Private Organizations for Women\u2019s Economic Rights Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To strengthen the public-private partnerships and policy efforts of the Department of State to advance women's economic security in South and Central Asia, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T09:18:39Z"
    }
  ]
}
```
