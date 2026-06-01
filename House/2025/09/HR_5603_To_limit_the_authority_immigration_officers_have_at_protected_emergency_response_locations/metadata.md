# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5603?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5603
- Title: Emergency Responder Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 5603
- Origin chamber: House
- Introduced date: 2025-09-26
- Update date: 2026-03-06T09:07:14Z
- Update date including text: 2026-03-06T09:07:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-26: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-26: Introduced in House

## Actions

- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-26",
    "latestAction": {
      "actionDate": "2025-09-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5603",
    "number": "5603",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "R000621",
        "district": "6",
        "firstName": "Emily",
        "fullName": "Rep. Randall, Emily [D-WA-6]",
        "lastName": "Randall",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Emergency Responder Protection Act",
    "type": "HR",
    "updateDate": "2026-03-06T09:07:14Z",
    "updateDateIncludingText": "2026-03-06T09:07:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
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
      "actionDate": "2025-09-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-26",
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
          "date": "2025-09-26T14:04:20Z",
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
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "TX"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "DC"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "IL"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "WA"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "True",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "MI"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "CA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "CA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "CA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "OR"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "OR"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "WA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5603ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5603\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Ms. Randall (for herself, Ms. Garcia of Texas , Ms. Norton , Ms. Kelly of Illinois , Ms. DelBene , Mr. Cisneros , Ms. Tlaib , Mr. Huffman , Ms. Lofgren , and Mr. Garcia of California ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo limit the authority immigration officers have at protected emergency response locations.\n#### 1. Short title\nThis Act may be cited as the Emergency Responder Protection Act .\n#### 2. Powers of immigration officers and employees at protected emergency response locations\n##### (a) In general\nSection 287 of the Immigration and Nationality Act ( 8 U.S.C. 1357 ) is amended by adding at the end the following:\n(i) (1) (A) An enforcement action may not take place at, be focused on, or occur within, 1,000 feet of a protected emergency response location, except under exigent circumstances. (B) If an immigration enforcement action is taking place under exigent circumstances, and the exigent circumstances permitting the enforcement action cease, the enforcement action shall be discontinued until such exigent circumstances reemerge. (C) If an individual referred to in subparagraph (A) or (B) of paragraph (2) is not certain as to whether exigent circumstances exist, the individual shall cease the enforcement action immediately, consult with their supervisor in real time as to the existence of exigent circumstances, and shall not continue the enforcement action until the individual\u2019s supervisor affirmatively confirms the existence of exigent circumstances. (2) This subsection shall apply to any enforcement action by\u2014 (A) officers or agents of the Department of Homeland Security, including officers and agents of U.S. Immigration and Customs Enforcement and U.S. Customs and Border Protection; and (B) any individual designated to perform immigration enforcement functions pursuant to subsection (g). (3) (A) When proceeding with an enforcement action at or near a protected emergency response location, individuals referred to in subparagraphs (A) and (B) of paragraph (2) shall make every effort\u2014 (i) to conduct themselves as discreetly as possible, consistent with officer and public safety; (ii) to limit the time spent at the protected emergency response location; and (iii) to limit the enforcement action to the person or persons for whom prior approval was obtained. (B) If, in the course of an enforcement action that is not initiated at or focused on a protected emergency response location, individuals referred to in subparagraphs (A) and (B) of paragraph (2) are led to or near a protected emergency response location, and no clear exigent circumstance with respect to the protected emergency response location exists, such individuals shall\u2014 (i) cease before taking any further enforcement action; (ii) conduct themselves in a discreet manner; (iii) maintain surveillance; and (iv) in the event that uncertainty exists about the existence of exigent circumstances, immediately consult their supervisor in order to determine whether such enforcement action should be discontinued pursuant to paragraph (1)(C). (C) This subsection shall not apply to the transportation of an individual apprehended at or near a land or sea border to a hospital or health care provider for the purpose of providing such individual medical care. (D) This subsection shall not apply to a rare premeditated arrest operation, undertaken with the prior written approval of an appropriate authorizing official, involving the targeted arrest of a terrorist suspect, an individual who poses a clear threat to national security, or an individual who poses an extraordinary danger to public safety. (4) If an enforcement action is carried out in violation of this subsection\u2014 (A) no information resulting from the enforcement action may be entered into the record or received into evidence in a removal proceeding resulting from the enforcement action; and (B) the alien who is the subject of such removal proceeding may file a motion for the immediate termination of the removal proceeding. (5) (A) Each official specified in subparagraph (B) shall ensure that the employees under the supervision of such official receive annual training in compliance with the requirements of this subsection, section 239, and section 384 of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1367 ). (B) The officials specified in this subparagraph are the following: (i) The Chief Counsel of U.S. Immigration and Customs Enforcement. (ii) The Field Office Directors of U.S. Immigration and Customs Enforcement. (iii) Each Special Agent in Charge of U.S. Immigration and Customs Enforcement. (iv) Each Chief Patrol Agent of U.S. Customs and Border Protection. (v) The Director of Field Operations of U.S. Customs and Border Protection. (vi) The Director of Air and Marine Operations of U.S. Customs and Border Protection. (vii) The Internal Affairs Special Agent in Charge of U.S. Customs and Border Protection. (6) (A) Not later than 30 days after any enforcement action is taken at a protected emergency response location by any individual referred to in subparagraph (A) or (B) of paragraph (2), the Secretary of Homeland Security shall provide a report to both the Office of the Inspector General of the Department of Homeland Security and the Office for Civil Rights and Civil Liberties of the Department of Homeland Security for each of these individual enforcement actions, which shall contain the following information: (i) The date, State, and local political subdivision (such as city, town, or county) in which each enforcement action occurred. (ii) The specific protected emergency response location site where the enforcement action occurred. (iii) The type of enforcement action that occurred. (iv) The specific department, agency, and officers responsible for the enforcement action. (v) A thorough description of the circumstances which purportedly justified the enforcement action, including either\u2014 (I) a clear description of the exigent circumstances involved; or (II) a certified copy of the written approval for the immigration arrest that was signed by an appropriate authorizing officer, along with a clear description of the specific and rare threat which justified the premeditated arrest at this protected emergency response location. (vi) A description of the intended target of the enforcement action. (vii) The number of individuals, if any, arrested or taken into custody through the enforcement action. (viii) The number of collateral arrests, if any, from the enforcement action and the reasons for each such arrest. (ix) A certification of whether a supervisor was contacted prior to, during, or after each such enforcement action. (B) An appropriate committee of Congress may, at any time, request, and the Secretary of Homeland Security shall provide, a confidential or redacted copy of one of the individual reports described in subparagraph (A). (7) (A) The Director of U.S. Immigration and Customs Enforcement and the Commissioner of U.S. Customs and Border Protection shall each submit to the appropriate committees of Congress each year a report on the enforcement actions undertaken by U.S. Immigration and Customs Enforcement and U.S. Customs and Border Protection, respectively, during the preceding year that were covered by this subsection. (B) Each report on an agency for a year under this paragraph shall set forth the following: (i) The number of enforcement actions at or focused on a protected emergency response location. (ii) The number of enforcement actions where officers or agents were subsequently led to or near a protected emergency response location. (iii) The date, site, State, and local political subdivision (such as city, town, or county) in which each enforcement action covered by clause (i) or (ii) occurred. (iv) The component of the agency responsible for each such enforcement action. (v) A description of the intended target of each such enforcement action. (vi) The number of individuals, if any, arrested or taken into custody through each such enforcement action. (vii) The number of collateral arrests, if any, from each such enforcement action and the reasons for each such arrest. (viii) A certification of whether the location administrator was contacted prior to, during, or after each such enforcement action. (8) (A) The Office of the Inspector General of the Department of Homeland Security shall submit to the appropriate committees of Congress each year a report on the complaints of enforcement actions taken in protected emergency response locations by U.S. Immigration and Customs Enforcement and U.S. Customs and Border Protection during the preceding year that were covered by this subsection. (B) Each report for a year under this paragraph shall set forth the following: (i) The number of complaints of enforcement actions reported at or focused on a protected emergency response location. (ii) The reported date, site, State, and local political subdivision (such as city, town, or county) in which each enforcement action covered was by clause (i) occurred. (iii) The reported agency responsible for each such enforcement action. (iv) A description of the intended target of each such enforcement action. (v) The reported number of individuals, if any, arrested or taken into custody through each such enforcement action. (vi) The reported number of collateral arrests, if any, from each such enforcement action and the reasons for each such arrest. (vii) If available, a certification of whether the location administrator was contacted prior to, during, or after each such enforcement action. (9) In this subsection: (A) The term active natural disaster includes\u2014 (i) floods, storms, wildfires, hurricanes, earthquakes, landslides, drought, volcanic eruptions, and tornadoes; and (ii) man-made disasters, such as oil spills and chemical spills. (B) The term appropriate authorizing official means the following: (i) In the case of officers and agents of U.S. Immigration and Customs Enforcement, one of the following officials: (I) The Assistant Director of Operations, Homeland Security Investigations. (II) The Executive Associate Director of Homeland Security Investigations. (III) The Assistant Director for Field Operations, Enforcement, and Removal Operations. (IV) The Executive Associate Director for Field Operations, Enforcement, and Removal Operations. (V) Any other individual who is determined to be an appropriate authorizing official by the Secretary of Homeland Security. (ii) In the case of officers and agents of U.S. Customs and Border Protection, one of the following officials: (I) A Chief Patrol Agent. (II) The Director of Field Operations. (III) The Director of Air and Marine Operations. (IV) The Internal Affairs Special Agent in Charge. (V) Any other individual who is determined to be an appropriate authorizing official by the Secretary of Homeland Security. (iii) In the case of all other individuals referred to in subparagraph (A) or (B) of paragraph (2), an official determined under rules promulgated by the Secretary of Homeland Security not later than 90 days after the date of the enactment of this subsection. (C) The term appropriate committees of Congress means\u2014 (i) the Committee on Homeland Security and Governmental Affairs of the Senate; (ii) the Committee on the Judiciary of the Senate; (iii) the Committee on Appropriations of the Senate; (iv) the Committee on Energy and Natural Resources of the Senate; (v) the Committee on Homeland Security of the House of Representatives; (vi) the Committee on the Judiciary of the House of Representatives; (vii) the Committee on Natural Resources of the House of Representatives; (viii) the Committee on Transportation and Infrastructure of the House of Representatives; and (ix) the Committee on Appropriations of the House of Representatives. (D) The term enforcement action means an apprehension, arrest, interview, request for identification, search, or surveillance for the purposes of immigration enforcement, and includes an enforcement action at, or focused on, a protected emergency response location that is part of a joint case led by another law enforcement agency. (E) The term exigent circumstances means a situation involving any of the following: (i) The imminent risk of death, violence, or physical harm to any person, including a situation implicating terrorism or the national security of the United States in some other manner. (ii) The immediate arrest or hot pursuit of an individual presenting an imminent danger to public safety, including the imminent risk of death, violence, or physical harm to a person. (iii) A rare, premeditated arrest operation described in paragraph (3)(D), undertaken with the prior written approval of an appropriate authorizing official, involving the targeted arrest of a terrorist suspect, an individual who poses a clear threat to national security, or an individual who poses an extraordinary danger to public safety. (iv) The imminent risk of destruction of evidence that is material to an ongoing criminal case. (F) The term protected emergency response location includes all of the physical space located within 1,000 feet of the following: (i) Locations where active natural disaster, human-caused events, emergency declarations are in effect, or emergency response and relief is being provided, such as the distribution of emergency supplies, food, and water; places of temporary shelter; along evacuation routes; and sites where registration for disaster-related assistance or family reunification is under way. (ii) Locations of any organization that provides disaster or emergency social services and assistance. (G) The term supervisor means an official determined under rules promulgated by the Secretary of Homeland Security not later than 90 days after the date of the enactment of this subsection. .\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect 90 days after the date of the enactment of this Act.\n##### (c) Rule making\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Homeland Security shall issue rules to carry out the amendment made by subsection (a).",
      "versionDate": "2025-09-26",
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
        "updateDate": "2025-12-16T19:37:15Z"
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
      "date": "2025-09-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5603ih.xml"
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
      "title": "Emergency Responder Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Emergency Responder Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To limit the authority immigration officers have at protected emergency response locations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T05:33:33Z"
    }
  ]
}
```
