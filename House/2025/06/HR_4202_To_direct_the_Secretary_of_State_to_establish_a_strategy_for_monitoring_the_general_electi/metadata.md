# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4202?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4202
- Title: Protect Honduran Democracy Act
- Congress: 119
- Bill type: HR
- Bill number: 4202
- Origin chamber: House
- Introduced date: 2025-06-26
- Update date: 2025-09-18T08:07:05Z
- Update date including text: 2025-09-18T08:07:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-26 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-26: Introduced in House

## Actions

- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-26 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4202",
    "number": "4202",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S000168",
        "district": "27",
        "firstName": "Maria",
        "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
        "lastName": "Salazar",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Protect Honduran Democracy Act",
    "type": "HR",
    "updateDate": "2025-09-18T08:07:05Z",
    "updateDateIncludingText": "2025-09-18T08:07:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
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
      "actionDate": "2025-06-26",
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
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T14:05:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-26T14:05:35Z",
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
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "TX"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "NJ"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
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
      "sponsorshipDate": "2025-06-26",
      "state": "NY"
    },
    {
      "bioguideId": "G000590",
      "district": "7",
      "firstName": "Mark",
      "fullName": "Rep. Green, Mark E. [R-TN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "TN"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4202ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4202\nIN THE HOUSE OF REPRESENTATIVES\nJune 26, 2025 Ms. Salazar (for herself, Mr. Castro of Texas , Mr. Smith of New Jersey , Mrs. Torres of California , Mr. Lawler , and Mr. Green of Tennessee ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of State to establish a strategy for monitoring the general elections in the Republic of Honduras to take place on November 30, 2025, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect Honduran Democracy Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe 2025 election process in the Republic of Honduras raises serious concerns about the fairness of the electoral process, including irregularities with the March 2025 primary election, violence against candidates and the actions undertaken by security and defense forces under the ongoing state of emergency, including serious human rights violations which undermine the conditions of the election;\n**(2)**\nthere is a need for the United States to support efforts to ensure elections in the Republic of Honduras to take place on November 30, 2025, are free and fair; and\n**(3)**\nthe Armed Forces of Honduras and other relevant institutions with a role in the electoral process should respect their role within the confines of the constitution of Honduras and protect the democratic process.\n#### 3. Strategy\n##### (a) In general\nThe Secretary of State shall establish a strategy to promote free and fair elections in Honduras to take place on November 30, 2025.\n##### (b) Matters To be included\nThe strategy required by subsection (a) shall include support for monitoring the elections by credible and internationally recognized elections monitoring bodies, such as the Organization of American States, the European Union, the United Nations, and experienced civil society observers and others to achieve the following:\n**(1)**\nEnsure that candidates to public office are not subject to harassment, undue legal persecution or other efforts to misuse State resources to dissuade them or undermine their candidacies.\n**(2)**\nAvoid the misuse of State resources aimed at influencing voter preferences.\n**(3)**\nAvoid the use of violence and intimidation, including by transnational criminal organizations, local gangs, or political parties and their proxies.\n**(4)**\nGuarantee freedom of speech and assembly.\n**(5)**\nEnsure transparent and credible transmission of elections results.\n#### 4. Assistance\nThe President, acting through the Secretary of State, is authorized to provide assistance on a grant basis to nongovernmental organizations for activities\u2014\n**(1)**\nto monitor the national elections in Honduras to take place on November 30, 2025; and\n**(2)**\nto assess the extent to which these elections are held on a free and fair basis.\n#### 5. Sanctions\n##### (a) In general\nThe President shall impose the sanctions described in subsection (b) with respect to any foreign person, including any current or former official of the Government of Honduras or any person acting on behalf of that Government, that the President determines\u2014\n**(1)**\nhas unduly prevented, or is responsible for ordering or otherwise directing the undue prevention of, any candidate, or prospective candidate, in the general elections in Honduras to take place on November 30, 2025;\n**(2)**\nhas knowingly materially assisted, sponsored, or provided significant financial, material, or technological support for, or goods or services in support of, the commission of the acts described in paragraph (1); or\n**(3)**\nhas carried out acts of intimidation or harassment toward candidates, election officials, or election observers, including through the use of spurious legal action.\n##### (b) Sanctions described\n**(1) In general**\nThe sanctions described in this subsection are, in the case of an alien determined by the President to be subject to subsection (a), denial of a visa to, and exclusion from the United States of, the alien, and revocation in accordance with section 221(i) of the Immigration and Nationality Act ( 8 U.S.C. 1201(i) ), of any visa or other documentation of the alien.\n**(2) Exceptions**\nThe sanctions described in paragraph (1) shall not apply with respect to a foreign person that\u2014\n**(A)**\nthe President determines is the subject of other sanctions equivalent to those described in paragraph (1); or\n**(B)**\nis an alien, if admitting the alien into the United States is necessary to permit the United States to comply with the Agreement regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States, or other applicable international obligations.\n##### (c) Waiver\nThe President may waive the application of sanctions under subsection (b) with respect to a foreign person if the President\u2014\n**(1)**\ndetermines that such a waiver is in the national interest of the United States; and\n**(2)**\non or before the date on which the waiver takes effect, submits to the Committee on Foreign Relations and the Committee on Appropriations of the Senate and the Committee on Foreign Affairs and the Committee on Appropriations of the House of Representatives a notice of and justification for the waiver.\n##### (d) Regulatory authority\nThe President shall issue such regulations, licenses, and orders as are necessary to carry out this section.\n#### 6. Promotion of migrant participation in elections\nCongress encourages the Secretary of State to promote the ability of citizens of Honduras residing in the United States to vote in the general elections in Honduras to take place on November 30, 2025.\n#### 7. Sense of Congress\nIt is the sense of Congress that the President should continue to seek to coordinate with other countries, particularly Central American countries, a comprehensive, multilateral strategy to further the purposes of this Act, including, as appropriate, encouraging other countries to take measures with respect to Honduras that are similar to measures described in this Act.\n#### 8. Authorization of appropriations\n##### (a) In general\nThere is authorized to be appropriated to carry out this Act $1,000,000 for each of the fiscal years 2026 and 2027.\n##### (b) Availability of funds\nAmounts appropriated pursuant to the authorization of appropriations under subsection (a) are authorized to remain available until expended.",
      "versionDate": "2025-06-26",
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
        "updateDate": "2025-07-29T21:34:41Z"
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
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4202ih.xml"
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
      "title": "Protect Honduran Democracy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-15T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect Honduran Democracy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-15T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of State to establish a strategy for monitoring the general elections in the Republic of Honduras to take place on November 30, 2025, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-15T04:18:30Z"
    }
  ]
}
```
