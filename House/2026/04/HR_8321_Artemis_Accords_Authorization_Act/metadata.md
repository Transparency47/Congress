# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8321?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8321
- Title: Artemis Accords Authorization Act
- Congress: 119
- Bill type: HR
- Bill number: 8321
- Origin chamber: House
- Introduced date: 2026-04-16
- Update date: 2026-04-22T08:07:35Z
- Update date including text: 2026-04-22T08:07:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-16: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2026-04-16: Introduced in House

## Actions

- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-16",
    "latestAction": {
      "actionDate": "2026-04-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8321",
    "number": "8321",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001217",
        "district": "23",
        "firstName": "Jared",
        "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
        "lastName": "Moskowitz",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Artemis Accords Authorization Act",
    "type": "HR",
    "updateDate": "2026-04-22T08:07:35Z",
    "updateDateIncludingText": "2026-04-22T08:07:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-16",
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
      "actionDate": "2026-04-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-16",
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
          "date": "2026-04-16T14:06:00Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "FL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "NY"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8321ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8321\nIN THE HOUSE OF REPRESENTATIVES\nApril 16, 2026 Mr. Moskowitz (for himself and Mrs. Luna ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo promote peaceful space exploration, expand participation in the Artemis Accords, establish norms for safe and sustainable space activities, and advance national security and economic competitiveness through leadership in space.\n#### 1. Short title\nThis Act may be cited as the Artemis Accords Authorization Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nThe United States has long been a global leader in space exploration, scientific discovery, and the development of technologies that benefit both national security and economic growth.\n**(2)**\nThe Artemis program, led by the National Aeronautics and Space Administration (NASA), represents the next phase of human space exploration, including returning humans to the Moon and establishing a sustainable presence for future missions to Mars.\n**(3)**\nThe Artemis Accords were first introduced in 2020 by NASA, in coordination with the Department of State and seven other initial signatory countries, including Australia, Canada, Italy, Japan, Luxembourg, the United Arab Emirates, and the United Kingdom.\n**(4)**\nOver the last five years, the Artemis Accords have expanded to 61 signatories.\n**(5)**\nThe Artemis Accords reinforce the commitment by signatory nations to foundational space law instruments\u2014including the Outer Space Treaty, the Registration Convention, and the Rescue and Return Agreement\u2014while also promoting best practices and norms for responsible civil space exploration and use.\n#### 3. Statement of policy\nIt is the policy of the United States\u2014\n**(1)**\nto promote the peaceful exploration and use of outer space, including the Moon and other celestial bodies, consistent with international law;\n**(2)**\nto strengthen international cooperation through the Artemis Accords as a framework for transparency, compatibility, and responsible behavior in space;\n**(3)**\nto maintain United States leadership in civil space exploration, scientific discovery, and commercial space development;\n**(4)**\nto support the development of norms and standards that ensure the safety, sustainability, and long-term viability of space activities;\n**(5)**\nto expand participation in the Artemis Accords among allies and partners, particularly in strategically significant regions;\n**(6)**\nto counter efforts by strategic competitors to shape space governance in ways that are inconsistent with democratic values, transparency, and the rule of law; and\n**(7)**\nto advance United States national security, economic competitiveness, and diplomatic engagement through sustained leadership in space exploration initiatives.\n#### 4. Special Coordinator for the Artemis Accords\n##### (a) In general\nThe Secretary of State is authorized to establish, carry out, and broaden the Artemis Accords espousing the principles set forth in section 3.\n##### (b) Special Coordinator\nThere shall be a Special Coordinator for the Artemis Accords, who shall be appointed by the Secretary of State and shall report to Assistant Secretary for Oceans, International Environment and Scientific Affairs.\n##### (c) Duties\nThe Special Coordinator shall be responsible for\u2014\n**(1)**\nleading diplomatic efforts to expand participation in the Artemis Accords;\n**(2)**\ncoordinating United States engagement with foreign governments, international organizations, and commercial partners regarding civil space cooperation;\n**(3)**\nsupporting the development of international norms governing lunar activities, space resource extraction, and space traffic management;\n**(4)**\ncoordinating with relevant United States agencies, including\u2014\n**(A)**\nthe National Aeronautics and Space Administration (NASA);\n**(B)**\nthe Department of Commerce;\n**(C)**\nthe Department of Defense; and\n**(D)**\nthe Office of Space Commerce;\n**(5)**\nengaging with United States industry stakeholders to advance public-private partnerships in support of the Artemis program; and\n**(6)**\nadvising the Department on strategies to ensure that United States leadership in space is aligned with broader foreign policy and national security objectives.\n#### 5. Report\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, and annually thereafter for four years, the Secretary of State, in coordination with the Administrator of NASA, shall submit to the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate, a report that includes\u2014\n**(1)**\na list of countries participating in the Artemis Accords and any new signatories during the reporting period;\n**(2)**\na description of diplomatic efforts undertaken by the United States to expand participation in the Artemis Accords;\n**(3)**\nan assessment of compliance by participating countries with the principles of the Artemis Accords;\n**(4)**\na description of ongoing and planned cooperative activities related to lunar exploration and other space missions;\n**(5)**\nan evaluation of the role of United States commercial entities in Artemis-related partnerships;\n**(6)**\nan assessment of challenges to international cooperation in space, including geopolitical competition, regulatory barriers, and technological compatibility;\n**(7)**\na description of efforts by the People\u2019s Republic of China and the Russian Federation to influence global space governance and how such efforts impact United States interests; and\n**(8)**\nrecommendations to strengthen United States leadership in international space cooperation.\n##### (b) Form\nThe report required by subsection (a) shall be submitted in unclassified form, but may include a classified annex.\n#### 6. Strategy\n##### (a) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nlow-earth orbit satellite technology is crucial for maintaining United States leadership in the 21st century in both military and civil technology domains;\n**(2)**\nlow-earth orbit satellite technology has potential to serve as an anti-censorship and pro free speech technology around the world;\n**(3)**\nlow-earth orbit satellite technology has incredible humanitarian potential to connect hundreds of millions people to the internet and the modern global economy; and\n**(4)**\ninstruments of the United States Government should be used to promote the export, use, and potential of American low-earth orbit satellite technology.\n##### (b) Strategy\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State, in coordination with the Chief Executive Officer of the United States International Development Finance Corporation, the Director of the United States Trade and Development Agency, and the heads of other Federal departments and agencies, as appropriate, shall submit to the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate a strategy on the integration of low-earth orbit satellite technologies and high-altitude platform systems into United States foreign policy.\n##### (c) Elements\nThe strategy required by subsection (b) shall include efforts and plans to\u2014\n**(1)**\nuse feasibility studies to promote low-earth orbit satellite technology as a form of connectivity;\n**(2)**\noffer loans, guarantees, insurance or other financial products to help countries procure low-earth orbit satellite technologies;\n**(3)**\ndirectly provide low-earth orbit satellite technologies to countries when consistent with the United States\u2019 national interest;\n**(4)**\nregulate, as appropriate, the export of controlled low-earth orbit satellite technologies to ensure continued American technological leadership and the misuse of the technology inconsistent with our policies and values; and\n**(5)**\nimpose possible restrictions on strategic competitor\u2019s alternatives to American low-earth orbit satellite technologies.\n##### (d) Form\nThe strategy required by subsection (b) shall be submitted in unclassified form, but may include a classified annex.",
      "versionDate": "2026-04-16",
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
        "updateDate": "2026-04-20T22:30:35Z"
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
      "date": "2026-04-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8321ih.xml"
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
      "title": "Artemis Accords Authorization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T14:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Artemis Accords Authorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-17T14:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To promote peaceful space exploration, expand participation in the Artemis Accords, establish norms for safe and sustainable space activities, and advance national security and economic competitiveness through leadership in space.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-17T14:03:30Z"
    }
  ]
}
```
