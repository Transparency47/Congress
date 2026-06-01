# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3981?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3981
- Title: BRAVE Burma Act
- Congress: 119
- Bill type: S
- Bill number: 3981
- Origin chamber: Senate
- Introduced date: 2026-03-04
- Update date: 2026-04-22T11:03:21Z
- Update date including text: 2026-05-09T16:27:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in Senate
- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2026-03-04: Introduced in Senate

## Actions

- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3981",
    "number": "3981",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "BRAVE Burma Act",
    "type": "S",
    "updateDate": "2026-04-22T11:03:21Z",
    "updateDateIncludingText": "2026-05-09T16:27:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-04",
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
          "date": "2026-03-04T16:38:46Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "sponsorshipDate": "2026-03-04",
      "state": "IN"
    },
    {
      "bioguideId": "M000355",
      "firstName": "Mitch",
      "fullName": "Sen. McConnell, Mitch [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "McConnell",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "KY"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "OR"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "MD"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3981is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3981\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2026 Mr. Van Hollen (for himself, Mr. Young , Mr. McConnell , and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo amend the Burma Unified through Rigorous Military Accountability Act of 2022 to extend the sunset, to require a determination with respect to the imposition of sanctions on certain persons of Burma, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bringing Real Accountability Via Enforcement in Burma Act or the BRAVE Burma Act .\n#### 2. Extension of sunset\nSection 5574(a) of the Burma Unified through Rigorous Military Accountability Act of 2022 (subtitle E of title LV of division E of the James M. Inhofe National Defense Authorization Act for Fiscal Year 2023; 22 U.S.C. 10225) is amended by striking 8 years and inserting 10 years .\n#### 3. Modifications to reporting requirement\nSection 5571(e) of the Burma Unified through Rigorous Military Accountability Act of 2022 (22 U.S.C. 10222(e)) is amended to read as follows:\n(e) Assessment and report on sanctions with respect to Burmese persons (1) In general Not later than 180 days after the date of the enactment of the Bringing Real Accountability Via Enforcement in Burma Act , and annually thereafter for 7 years, the President shall determine whether the following persons meet the criteria for sanctions described under subsection (a) or under Executive Order 14014 (86 Fed. Reg. 9429; relating to blocking property with respect to the situation in Burma): (A) Any Burmese state-owned enterprise described in subsection (c)(2). (B) Myanma Economic Bank. (C) Any foreign person that the President determines operates in the jet fuel sector of the Burmese economy, including through activities such as the provision of financial services or the importation, exportation, reexportation, sale, supply, trade, storage, or transport, directly or indirectly, of jet fuel in Burma. (2) Report required Upon making the determination required by paragraph (1), the President shall submit to the appropriate congressional committees a report on the assessment. (3) Form of report The report required by paragraph (2) shall be submitted in unclassified form but may include a classified annex. .\n#### 4. Limitation of shareholding benefitting the State Security and Peace Commission\n##### (a) In general\nThe Secretary of the Treasury shall instruct the United States Executive Director at the International Monetary Fund to use the voice and vote of the United States, when assessing potential changes to any shareholding formula in connection with a governance review of the Fund, to limit, as appropriate, an increase to the shareholding of Burma if the country is subject to the rule of the State Security and Peace Commission or any successor governing authority.\n##### (b) Waiver\nThe President of the United States may waive the application of subsection (a) upon certifying to the Committee on Financial Services of the House of Representatives and the Committee on Foreign Relations of the Senate that the waiver is important to the national interest of the United States, with a detailed explanation of the reasons therefor.\n#### 5. United States Special Envoy for Burma\n##### (a) In general\nThe Secretary of State shall appoint a Special Envoy for Burma, who shall\u2014\n**(1)**\nhave the rank and status of ambassador; and\n**(2)**\nbe responsible for coordinating all aspects of United States policy with respect to Burma.\n##### (b) Qualifications\nThe Secretary\u2014\n**(1)**\nshall appoint the Special Envoy from among recognized experts in matters relating to Burma; and\n**(2)**\nmay appoint a Foreign Service Officer as the Special Envoy.\n##### (c) Central objective\nThe Special Envoy should develop a comprehensive strategy for the implementation of the full range of United States diplomatic capabilities to promote the restoration of peace and a civilian-led democratic government in Burma.\n##### (d) Duties and responsibilities\nThe Special Envoy shall also\u2014\n**(1)**\ncoordinate the sanctions policies of the United States under the Burma Unified through Rigorous Military Accountability Act of 2022 (22 U.S.C. 10201 et seq.) and other relevant statutory authorities across relevant Federal departments and agencies;\n**(2)**\ndevelop and implement a comprehensive international effort to impose and enforce multilateral sanctions with respect to Burma;\n**(3)**\nlead interagency United States Government efforts, including efforts of the Chief of Mission in Burma, the Ambassador to ASEAN, the Ambassador to Bangladesh, the Ambassador to India, and the United States Permanent Representative to the United Nations, relating to\u2014\n**(A)**\nidentifying opportunities to coordinate with and exert pressure on the governments of the People\u2019s Republic of China and the Russian Federation to cease or curtail support for the Burmese military;\n**(B)**\nworking with like-minded partners to impose a coordinated arms embargo on the Burmese military and targeted sanctions on the economic interests of the Burmese military, including through the introduction and adoption of a United Nations Security Council resolution;\n**(C)**\nengaging Burmese civil society, democracy advocates, ethnic nationality representative groups, and organizations or groups representing the resistance and revolutionary movement, as well as officials elected in 2020 such as the Committee Representing the Pyidaungsu Hluttaw, the National Unity Government, the National Unity Consultative Council, the Ethnic Resistance Revolutionary Organizations, and their designated representatives;\n**(D)**\nencouraging the United Nations Independent Investigative Mechanism for Myanmar to incorporate accountability mechanisms in relation to the atrocities against Rohingya and other ethnic groups, to take further steps to make its leadership and membership ethnically diverse, and to incorporate measures to enhance ethnic reconciliation and national unity into its policy agenda;\n**(E)**\nassisting efforts by the relevant United Nations Special Procedures to secure the release of all political prisoners in Burma, promote respect for human rights, seek accountability, and encourage dialogue;\n**(F)**\nworking with the governments of India, Bangladesh, and other countries as appropriate to address challenges in Western Burma, including issues related to atrocity crimes, refugees and displaced persons, cross-border humanitarian assistance and trade, trafficking in persons, illicit trafficking of narcotics and weapons, or other transnational threats to regional peace and security; and\n**(G)**\nsupporting nongovernmental organizations operating in Burma and neighboring countries working to restore civilian democratic rule to Burma, address the urgent humanitarian needs of the people of Burma, and build resilience against malign foreign influence in support of the military regime;\n**(4)**\nsupport protection, humanitarian assistance, and accountability efforts for ethnic minorities in Burma and the surrounding region;\n**(5)**\ncoordinate all streams of United States assistance to the people of Burma until such time as the United States normalizes diplomatic relations with Burma;\n**(6)**\nprovide timely input for reporting on the impacts of the implementation of the Burma Unified through Rigorous Military Accountability Act of 2022 on the Burmese military and the people of Burma; and\n**(7)**\nreport to and coordinate with Congress.",
      "versionDate": "",
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
        "actionDate": "2026-02-11",
        "text": "Received in the Senate and Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "3190",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "BRAVE Burma Act",
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
        "name": "International Affairs",
        "updateDate": "2026-03-20T15:13:04Z"
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
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3981is.xml"
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
      "title": "BRAVE Burma Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-22T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "BRAVE Burma Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Bringing Real Accountability Via Enforcement in Burma Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Burma Unified through Rigorous Military Accountability Act of 2022 to extend the sunset, to require a determination with respect to the imposition of sanctions on certain persons of Burma, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:18:24Z"
    }
  ]
}
```
