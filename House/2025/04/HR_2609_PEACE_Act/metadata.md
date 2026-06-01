# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2609?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2609
- Title: PEACE Act
- Congress: 119
- Bill type: HR
- Bill number: 2609
- Origin chamber: House
- Introduced date: 2025-04-02
- Update date: 2026-03-31T20:26:21Z
- Update date including text: 2026-03-31T20:26:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-02: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-04-02: Introduced in House

## Actions

- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-02",
    "latestAction": {
      "actionDate": "2025-04-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2609",
    "number": "2609",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001190",
        "district": "10",
        "firstName": "Bradley",
        "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
        "lastName": "Schneider",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "PEACE Act",
    "type": "HR",
    "updateDate": "2026-03-31T20:26:21Z",
    "updateDateIncludingText": "2026-03-31T20:26:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-02",
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
      "actionDate": "2025-04-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-02",
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
          "date": "2025-04-02T22:00:20Z",
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
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "AZ"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "PA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NJ"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2609ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2609\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2025 Mr. Schneider (for himself and Mr. Hamadeh of Arizona ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo promote education and training to United States diplomatic personnel relating to the Abraham Accords and other normalization agreements with Israel, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Promoting Education on the Abraham Accords for Comprehensive Engagement Act or the PEACE Act .\n#### 2. Sense of congress\nIt is the sense of Congress that\u2014\n**(1)**\neducating relevant Federal officials on the provisions of the Abraham Accords, as well as the provisions of prior normalization agreements with Israel, is essential to advancing the United States commitment to peace, cooperation, and stability in the Middle East;\n**(2)**\nthe Secretary of State should ensure that United States diplomats and related personnel working in the region or on related issues receive comprehensive training on the history, principles, and future applications of the Abraham Accords and other normalization agreements; and\n**(3)**\nthe Secretary of State should ensure that United States diplomats are taught about the policy codified in section 104 of the Israel Relations Normalization Acts of 2022 and future iterations of the policy as amended.\n#### 3. Abraham Accords and normalization education and training\n##### (a) In general\nTo carry out the policy described in section 2, the Secretary of State may undertake the following:\n**(1)**\nSupplementing existing offerings at the Foreign Service Institute and other relevant Department of State training facilities with courses focused on the Abraham Accords, peace agreements with Egypt and Jordan, and other such normalization agreements relating to Israel as determined by the Secretary of State. Such courses shall be developed to provide an understanding of these agreements\u2019 diplomatic history, implementation strategies, and implications for regional peace.\n**(2)**\nDeveloping virtual training modules and interactive content accessible by employees and officers of the Department of State worldwide, focused on the principles, history, and diplomatic impacts of these agreements.\n##### (b) Scope of training\nFor purposes of training and education activities implementing subsection (a)(2), the Secretary of State shall determine the countries eligible to provide such training in a manner that ensures alignment with current diplomatic landscape and objectives.\n#### 4. Fellowships and exchanges\nThe Director General of the Foreign Service is authorized to award fellowships or grants to eligible Foreign Service officers participating in programs, projects, or activities engaging with appropriate counterparts of Abraham Accords and other normalization agreement countries, as determined by the Secretary of State pursuant to section 3(b) , or engaging with regional organizations in the Middle East, including\u2014\n**(1)**\nshort-term and long-term fellowships with educational institutions, nongovernmental organizations, or diplomatic organizations involved in the negotiation and implementation of the Abraham Accords and other agreements; and\n**(2)**\nopportunities to collaborate with regional governmental and non-governmental institutions that are part of the Abraham Accords or have normalized relations with Israel.\n#### 5. Abraham accords and normalization advisory board\n##### (a) Establishment\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State shall establish a nonpartisan Abraham Accords and Normalization Advisory Board consisting of 4 individuals with expertise in diplomacy, Middle Eastern studies, interfaith dialogue, and peace-building.\n##### (b) Membership\nThe members of the Abraham Accords and Normalization Advisory Board shall be appointed as follows:\n**(1)**\nOne member each by the Chairperson and Ranking Member of the Committee on Foreign Affairs of the House of Representatives.\n**(2)**\nOne member each by the Chairperson and Ranking Member of the Committee on Foreign Relations of the Senate.\n##### (c) Duties\nThe Board shall be responsible for providing on a unanimous basis independent advice and recommendations on curriculum development, resource management, and strategic planning for education and training curricula within the Foreign Service Institute and the Department of State relating to the Abraham Accords and other normalization agreements.\n#### 6. Strategy and reporting requirements\n##### (a) In general\nNot later than 1 year after the enactment of this Act, the Secretary of State shall develop and submit to the appropriate congressional committees a strategy for the Department of State to implement comprehensive training and education programs focused on the Abraham Accords and other normalization agreements with Israel.\n##### (b) Elements\nThe strategy shall include:\n**(1)**\nA plan for integrating education on the Abraham Accords and other normalization agreements into existing training frameworks for Foreign Service Officers and other personnel of the Department of State;\n**(2)**\nA description of the unanimous recommendations of the Abraham Accords and Normalization Advisory Board established pursuant to section 5 and a detailed explanation of any departure from such recommendations in the course of implementing the education and training required by this Act.\n**(3)**\nAn outline of training requirements and goals to promote the understanding and operational capacity of United States personnel working with or on issues related to Abraham Accords and normalization agreements in the relevant countries; and\n**(4)**\nAn analysis of the manner and extent to which the implementation of the education and training required by this Act supports the strategy required by section 105 of the Israel Relations Normalization Act of 2022 (division Z of the Consolidated Appropriations Act, 2022; 22 U.S.C. 8601 note).\n##### (c) Ongoing reports\nNot later than 1 year after the submission of the report required by subsection (a), and annually thereafter for 4 years, the Secretary of State shall submit to the appropriate congressional committees a report detailing the progress, challenges, and measurable outcomes of the educational initiatives developed pursuant to this Act.\n##### (d) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Foreign Affairs and the Committee on Appropriations of the House of Representatives; and\n**(2)**\nthe Committee on Foreign Relations and the Committee on Appropriations of the Senate.",
      "versionDate": "2025-04-02",
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
        "updateDate": "2025-05-14T16:05:27Z"
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
      "date": "2025-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2609ih.xml"
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
      "title": "PEACE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T03:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PEACE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-09T03:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Promoting Education on the Abraham Accords for Comprehensive Engagement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-09T03:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To promote education and training to United States diplomatic personnel relating to the Abraham Accords and other normalization agreements with Israel, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-09T03:33:18Z"
    }
  ]
}
```
