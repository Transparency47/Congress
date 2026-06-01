# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1848?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1848
- Title: Houthi Human Rights Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 1848
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2026-05-27T17:31:52Z
- Update date including text: 2026-05-27T17:31:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-05 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-03 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-03 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 49 - 0.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-05 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-03 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-03 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 49 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1848",
    "number": "1848",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "I000056",
        "district": "48",
        "firstName": "Darrell",
        "fullName": "Rep. Issa, Darrell [R-CA-48]",
        "lastName": "Issa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Houthi Human Rights Accountability Act",
    "type": "HR",
    "updateDate": "2026-05-27T17:31:52Z",
    "updateDateIncludingText": "2026-05-27T17:31:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-03",
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
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 49 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-03",
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
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
            "date": "2025-12-03T16:06:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-05T15:05:15Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-05T15:05:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "VA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1848ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1848\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Issa (for himself, Mr. Sherman , Mr. Lawler , Mr. Schneider , Mr. Moskowitz , and Mr. Keating ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo authorize the imposition of sanctions with respect to the Houthis, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Houthi Human Rights Accountability Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nHouthi efforts to indoctrinate Yemenis into a violent, anti-Semitic, and extremist worldview are a threat to a Yemeni-led peace process and to regional stability; and\n**(2)**\nit is counter to United States policy to provide support to the Houthis in Yemen, including by supporting any efforts by the Houthis to indoctrinate, coerce, or force Yemenis to conform to their violent, anti-Semitic, and extremist worldview.\n#### 3. Report on Houthi indoctrination\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State, in consultation with the Administrator of the United States Agency for International Development, shall submit to the appropriate congressional committees a report on\u2014\n**(1)**\nHouthi efforts to indoctrinate Yemenis into a violent, anti-Semitic, or extremist worldview; and\n**(2)**\nthe long-term threat this indoctrination campaign poses to regional stability.\n#### 4. Report on obstacles to provision of humanitarian aid in areas of Yemen under de-facto Houthi control\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State, in consultation with the Administrator of the United States Agency for International Development, shall submit to the appropriate congressional committees a report on obstacles to the provision of humanitarian aid by international organizations and nongovernmental organizations in areas of Yemen under de-facto Houthi control.\n##### (b) Matters To be included\nThe report required by subsection (a) shall include the following:\n**(1)**\nAn identification of challenges to distribution of humanitarian aid created by Houthi-enforced rules, regulations, and bureaucracy with respect to access, and freedom of movement, and the overall impact on such rules, regulations, and bureaucracy have on the international community\u2019s ability to distribute such aid in a manner consistent with basic humanitarian principles.\n**(2)**\nAn assessment of attempted Houthi interference in the delivery of humanitarian aid, including the manipulation or undue influence of beneficiary lists or related data for political or military purposes, and the implications of any interference on civilian needs and aid distribution.\n**(3)**\nAn evaluation of the Houthis\u2019 use of violence and intimidation against humanitarian workers and diplomats, including current and former United States Embassy locally employed staff.\n**(4)**\nAn overview of the steps the United States and its partners are taking to ensure humanitarian assistance is delivered unhindered and consistent with basic humanitarian principles, including how United States-supported organizations respond to attempted Houthi diversion or interference.\n**(5) Scope**\nThe report required by subsection (a) shall address the period beginning on January 1, 2020, and ending on the date that is 90 days after the date of the enactment of this Act.\n#### 5. Report on human rights abuses committed by the Houthis\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State shall submit to the appropriate congressional committees a report on human rights abuses committed by the Houthis, including gender-based discrimination and violence, including\u2014\n**(1)**\nmahram regulations;\n**(2)**\nrecruitment and use of child soldiers;\n**(3)**\nenforced disappearance;\n**(4)**\nprolonged and arbitrary detention;\n**(5)**\nconduct that amounts to torture; and\n**(6)**\nunlawful killing.\n##### (b) Scope\nThe report required by subsection (a) shall address the period beginning on March 1, 2015, and ending on the date that is 90 days after the date of the enactment of this Act.\n#### 6. Sanctions authorized under the Global Magnitsky Human Rights and Accountability Act\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter, the Secretary of State, in consultation with the Secretary of the Treasury, shall submit to the appropriate congressional committees a determination on whether foreign persons described in subsection (b) meet the criteria for sanctions authorized under the Global Magnitsky Human Rights and Accountability Act ( 22 U.S.C. 2656 note), including with respect to acts that constitute gross violations of internationally recognized human rights as defined in section 502B(d)(1) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2304(d)(1) ).\n##### (b) Persons described\nA foreign person described in this subsection is a foreign person that\u2014\n**(1)**\nis a member of the Houthis; and\n**(2)**\nknowingly\u2014\n**(A)**\nimposes arbitrary or unlawful restriction on the delivery of humanitarian assistance in Yemen; or\n**(B)**\nengages in the human rights abuses described in section 5(a).\n#### 7. Sanctions authorized under the Robert Levinson Hostage Taking and Accountability Act\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter, the Secretary of State, in consultation with the Secretary of the Treasury, shall submit to the appropriate congressional committees a determination on whether foreign persons described in subsection (b) meet the criteria for sanctions authorized under the Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act ( 22 U.S.C. 1741 et seq. ), and Executive Order 14078.\n##### (b) Persons described\nA foreign person described in this subsection is a foreign person that\u2014\n**(1)**\nis a member of the Houthis; and\n**(2)**\n**(A)**\nis responsible for or is complicit in, or responsible for ordering, controlling, or otherwise directing, the hostage-taking of a United States national abroad or the unlawful or wrongful detention of a United States national abroad; or\n**(B)**\nknowingly provides financial, material, or technological support for, or goods or services in support of, an activity described in subparagraph (A).\n#### 8. Sunset\nThis Act shall terminate on the date that is 5 years after the date of the enactment of this Act.\n#### 9. Definitions\nIn this Act\u2014\n**(1)**\nthe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs and the Committee on Appropriations of the House of Representatives; and\n**(B)**\nthe Committee on Foreign Relations and the Committee on Appropriations of the Senate;\n**(2)**\nthe term foreign person means a person that is not a United States person;\n**(3)**\nthe term Houthis refers to persons officially known as Ansarallah ;\n**(4)**\nthe term person means and individual or entity; and\n**(5)**\nthe term United States person means\u2014\n**(A)**\na national of the United States;\n**(B)**\nan alien who is lawfully present in the United States; or\n**(C)**\nan entity organized under the laws of the United States or of any jurisdiction within the United States, including a foreign branch of such an entity.",
      "versionDate": "2025-03-05",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-12-11",
        "text": "Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "3451",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Houthi Human Rights Accountability Act",
      "type": "S"
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
            "updateDate": "2026-05-27T17:31:19Z"
          },
          {
            "name": "Foreign aid and international relief",
            "updateDate": "2026-05-27T17:31:26Z"
          },
          {
            "name": "Human rights",
            "updateDate": "2026-05-27T17:31:33Z"
          },
          {
            "name": "Sanctions",
            "updateDate": "2026-05-27T17:31:42Z"
          },
          {
            "name": "Yemen",
            "updateDate": "2026-05-27T17:31:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-05-16T17:51:43Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1848ih.xml"
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
      "title": "Houthi Human Rights Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-19T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Houthi Human Rights Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-19T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the imposition of sanctions with respect to the Houthis, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-19T04:33:20Z"
    }
  ]
}
```
