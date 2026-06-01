# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8320?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8320
- Title: USA 6G Global Leadership Act
- Congress: 119
- Bill type: HR
- Bill number: 8320
- Origin chamber: House
- Introduced date: 2026-04-16
- Update date: 2026-05-20T12:05:25Z
- Update date including text: 2026-05-20T12:05:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-16: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported by the Yeas and Nays: 41 - 2.
- Latest action: 2026-04-16: Introduced in House

## Actions

- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported by the Yeas and Nays: 41 - 2.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8320",
    "number": "8320",
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
    "title": "USA 6G Global Leadership Act",
    "type": "HR",
    "updateDate": "2026-05-20T12:05:25Z",
    "updateDateIncludingText": "2026-05-20T12:05:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 41 - 2.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
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
        "item": [
          {
            "date": "2026-04-22T20:28:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-04-16T14:02:10Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "SC"
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
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8320ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8320\nIN THE HOUSE OF REPRESENTATIVES\nApril 16, 2026 Ms. Johnson of Texas (for herself and Mrs. Biggs of South Carolina ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require additional duties of the Ambassador at Large for Cyberspace and Digital Policy with respect to United States diplomatic efforts ahead of certain international conferences, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the USA 6G Global Leadership Act .\n#### 2. Sense of congress\nIt is the Sense of Congress that\u2014\n**(1)**\nthe United States has a national security, economic, and foreign policy interest in winning the race for 6G global leadership;\n**(2)**\nthe People\u2019s Republic of China\u2019s (PRC) use of malign nonmarket practices to accelerate its development of 5G and 6G technology is coercive and constrains countries\u2019 access to reliable and secure telecommunications services;\n**(3)**\nthe United States government should leverage economic and diplomatic tools to ensure United States companies are positioned to compete as leading providers of 6G technology and are not unfairly disadvantaged by PRC based state owned enterprises;\n**(4)**\nit is in the United States interest to engage at the International Telecommunications Union (ITU) and private standard setting bodies to ensure the United States is positioned to lead on the key telecommunications, information, and other emerging technologies, including artificial intelligence; and\n**(5)**\nit is critical to cooperate with like-minded allies and partners, including through multilateral coordination, to promote secure telecommunications networks by achieving market leadership for trusted vendors.\n#### 3. Ambassador at Large for Cyberspace and Digital Policy responsibilities at Plenipotentiary Conference and World Radiocommunication Conference\n##### (a) Coordinator\nThe Ambassador at Large for Cyberspace and Digital Policy (authorized under subsection (i) of section 1 of the State Department Basic Authorities Act of 1956; 22 U.S.C. 2651a(i) ) shall coordinate and lead United States diplomatic efforts ahead of the Plenipotentiary Conference of the International Telecommunications Union (ITU) in 2026 and the World Radiocommunication Conference 2027.\n##### (b) Duties\nIn carrying out the coordination required by subsection (a), the Ambassador at Large for Cyberspace and Digital Policy shall be responsible for\u2014\n**(1)**\ncoordinating across the Department of State, the Department of Commerce, and other Federal departments and agencies, as appropriate, to promote candidates for election to the ITU\u2019s leadership bodies that support the United States economic and security objectives for increased telecommunications security, digital freedom, and information technology governance and standards;\n**(2)**\nconsulting with United States private sector entities to ensure that views and perspectives are understood, incorporated, and represented as the Department of State engages in the ITU elections process;\n**(3)**\nconsulting with Congress by providing quarterly briefings on developments leading up to the ITU elections and the World Radiocommunication Conference 2027;\n**(4)**\ncoordinating across the Department of State, the Department of Commerce, and other Federal departments and agencies, as appropriate, to advance United States interests ahead of the World Radiocommunication Conference 2027;\n**(5)**\nconducting diplomatic outreach to promote United States interests in the field of international telecommunications; and\n**(6)**\nother such duties that the Secretary of State may prescribe.\n##### (c) Report\n**(1) In general**\nNot later than 90 days after the date of the enactment of this Act, the Secretary of State shall develop and submit to the appropriate congressional committees a report on efforts by the People\u2019s Republic of China and by the Russian Federation to\u2014\n**(A)**\nleverage the ITU or other international forums to promote policies or standards that constrain digital freedom;\n**(B)**\nexpand the mandate of the ITU to cover internet governance policy, including by proposing internet governance standards at the ITU;\n**(C)**\nleverage their private sector\u2019s influence over developing countries to compel such countries to deliver favorable decisions on standards proposals, election victories, candidate selection, and other decisions at the ITU; and\n**(D)**\nuse the influence of Chinese or Russian nationals serving in the ITU to advantage companies, standards decisions, and ITU leadership candidates that advance the interests of the People\u2019s Republic of China or the Russian Federation, respectively.\n**(2) Form**\nThe report required by this subsection shall be submitted in unclassified form but may include a classified annex.\n**(3) Appropriate congressional committees defined**\nIn this subsection, the term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs and the Committee on Energy and Commerce of the House of Representatives; and\n**(B)**\nthe Committee on Foreign Relations and the Committee on Commerce, Science, and Transportation of the Senate.\n##### (d) Sunset\nThe authorities and requirements under this section shall expire upon the conclusion of the World Radiocommunication Conference 2027.\n#### 4. Project assistance\n##### (a) In general\nThe Secretary of State, in coordination with the Chief Executive Officer of the International Development Finance Corporation and the Director of the United States Trade and Development Agency, should carry out projects that assert United States global leadership in telecommunications infrastructure.\n##### (b) Priority projects\nFor assistance pursuant to subsection (a), the Secretary of State shall prioritize projects that\u2014\n**(1)**\npromote connectivity and use of trusted vendors in developing countries; and\n**(2)**\nuse technology produced by United States companies or entities if not specifically important that they are incorporated or by companies organized under the laws of United States allies if United States technology goods and services are not available.\n##### (c) Forms of support\nThe projects carried under this section may receive support through the following methods:\n**(1)**\nEarly-stage project development including feasibility studies.\n**(2)**\nDevelopment loans.\n**(3)**\nDirect investments in companies or projects that advance Unites States foreign policy interests.\n**(4)**\nOther types of support as appropriate.\n##### (d) Report\nNot later than 1 year after the date of the enactment of this Act, the Secretary of State shall submit to Congress a report that describes the projects undertaken pursuant to subsection (b).\n#### 5. 6G technology dominance strategy\n##### (a) Strategy for 6G technology dominance\nNot later than 90 days after the date of the enactment of this Act, the Secretary of State shall submit to the Committee on Foreign Affairs and the Committee on Energy and Commerce of the House of Representatives and the Committee on Foreign Relations and the Committee on Commerce, Science, and Transportation of the Senate a report that details the United States strategy to promote and dominate 6G technology globally.\n##### (b) Elements\nThe report required by subsection (a) shall also include a description and analysis of the activities of the Department of State regarding\u2014\n**(1)**\nactions to deepen cooperation with like-minded countries to promote United States and allied market leadership in 6G networks and technologies;\n**(2)**\nefforts to coordinate and cooperate with relevant Federal departments and agencies as well as United States-based private sector entities to plan, strategize, and conduct diplomatic engagements at telecommunication standard-setting bodies and organizations; and\n**(3)**\nthe effects on and impact of competition in artificial intelligence and other critical or emerging technologies, including the role of low-earth orbit satellites, in ensuring that the United States remains the partner of choice in 6G infrastructure.\n##### (c) Form\nThe report required by this section shall be submitted in unclassified form, but may include a classified annex.",
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
        "updateDate": "2026-04-20T22:30:53Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8320ih.xml"
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
      "title": "USA 6G Global Leadership Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T14:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "USA 6G Global Leadership Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-17T14:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require additional duties of the Ambassador at Large for Cyberspace and Digital Policy with respect to United States diplomatic efforts ahead of certain international conferences, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-17T14:03:27Z"
    }
  ]
}
```
