# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7870?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7870
- Title: ICE Standards Act
- Congress: 119
- Bill type: HR
- Bill number: 7870
- Origin chamber: House
- Introduced date: 2026-03-09
- Update date: 2026-04-01T16:19:20Z
- Update date including text: 2026-04-01T16:19:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-09: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-03-09: Introduced in House

## Actions

- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7870",
    "number": "7870",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "ICE Standards Act",
    "type": "HR",
    "updateDate": "2026-04-01T16:19:20Z",
    "updateDateIncludingText": "2026-04-01T16:19:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-09",
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
          "date": "2026-03-09T17:00:25Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7870ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7870\nIN THE HOUSE OF REPRESENTATIVES\nMarch 9, 2026 Mr. Gottheimer introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo require immigration enforcement reforms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the ICE Standards Act .\n#### 2. Immigration enforcement reforms\n##### (a) Training standards\n**(1) Standards**\nNot later than 180 days after the date of enactment of this Act, the Secretary of Homeland Security shall submit a report to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate describing the standards, policies, and practices governing the training of immigration officers (as such term is defined in section 101(a) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a) )).\n**(2) Training**\nThe Secretary of Homeland Security shall require each immigration officer to complete training not less than once a year, including web based, classroom, and tactical instruction, on updated policies on use of force and applicable legal developments, and training designed to\u2014\n**(A)**\npromote sound judgment and responsible decision-making in the application of both nonlethal and lethal force;\n**(B)**\nemphasize and practice de-escalation strategies to mitigate risk to officers and the public;\n**(C)**\nensure that the immigration officer is educated on rights protected under the First Amendment, including those of members of the press, demonstrators, and individuals engaged in lawful assembly, and performs duties in accordance with such protections; and\n**(D)**\nensure searches and seizures are conducted consistent with the Fourth Amendment.\n##### (b) Body worn and dashboard cameras\n**(1) In general**\nThe Secretary of Homeland Secretary shall require the use of\u2014\n**(A)**\nbody-worn cameras by all immigration officers; and\n**(B)**\ndashboard cameras for all vehicles being used in Federal immigration enforcement operations.\n**(2) Right to review footage**\nAn immigration officer has the right to review footage captured by body-worn cameras and dashboard cameras.\n##### (c) ID for all officers unless undercover\n**(1) Identification**\nThe Secretary of Homeland Security shall require each immigration officer to wear a uniform or identification clearly displaying the immigration officer or the name of the agency in which the officer is employed, unless\u2014\n**(A)**\nthere is a public safety or national security threat;\n**(B)**\nnot wearing identification is necessary to carry out the operation safely; or\n**(C)**\nthe personnel receives prior written approval from a supervisory officer.\n**(2) Prohibition**\nAn immigration officer may not wear a uniform that bears any identifier as police , unless the uniform clearly displays the name of the agency in which the officer is employed.\n##### (d) Sensitive Locations\nSection 287 of the Immigration and Nationality Act ( 8 U.S.C. 1357 ) is amended by adding at the end the following:\n(i) (1) Except as provided in paragraph (2), an officer or an agent of U.S. Immigration and Customs Enforcement or U.S. Customs and Border Protection may not perform an immigration enforcement action in a protected area. (2) This subsection shall not apply\u2014 (A) under exigent circumstances, including an immigration enforcement action that involves a national security threat, the pursuit of an individual who poses an imminent public safety threat, or the pursuit of an individual entering or attempting to enter the United States in the presence of the officer or agent; (B) under circumstances that involves the imminent risk of death, violence, or physical harm to a person or the imminent risk that evidence material to a criminal case will be destroyed; or (C) where a safe alternative location does not exist outside of the protected area. (3) The term protected area means any school, any hospital, medical facility, mental health facility, any place of worship or religious study (including permanent or temporary locations), and any polling place or voting site. .\n##### (e) Minimize risk\nThe Secretary of Homeland Security shall require each immigration officer to make all reasonable efforts to de-escalate tensions prior to using force.\n##### (f) Impose strict prohibition on the arrest and deportation of American citizens\n**(1) Verification**\nThe Secretary of Homeland Security shall require each immigration officer to verify citizenship status of an individual prior to arrest.\n**(2) Limitation on deportation**\nA national of the United States may not be deported from the United States.\n##### (g) Notification of local law enforcement\n**(1) In general**\nThe Secretary of Homeland Security shall notify local law enforcement agencies of impending Federal immigration enforcement operations in their jurisdiction at least one day before such operation occurs.\n**(2) Coordination**\nThe Secretary of Homeland Security shall make every effort to coordinate the operations Federal immigration officers with State and local law enforcement.",
      "versionDate": "2026-03-09",
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
        "name": "Immigration",
        "updateDate": "2026-04-01T16:19:20Z"
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
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7870ih.xml"
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
      "title": "ICE Standards Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T03:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ICE Standards Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-26T03:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require immigration enforcement reforms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T03:03:27Z"
    }
  ]
}
```
