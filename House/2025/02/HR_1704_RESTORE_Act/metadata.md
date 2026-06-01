# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1704?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1704
- Title: RESTORE Act
- Congress: 119
- Bill type: HR
- Bill number: 1704
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-02-06T19:41:24Z
- Update date including text: 2026-02-06T19:41:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1704",
    "number": "1704",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "K000400",
        "district": "37",
        "firstName": "Sydney",
        "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
        "lastName": "Kamlager-Dove",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "RESTORE Act",
    "type": "HR",
    "updateDate": "2026-02-06T19:41:24Z",
    "updateDateIncludingText": "2026-02-06T19:41:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:05:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "FL"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "IL"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NJ"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "OH"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NJ"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "OH"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "GA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "IL"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "MI"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "IL"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "FL"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1704ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1704\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Ms. Kamlager-Dove (for herself, Mr. Soto , Mr. Jackson of Illinois , Mrs. McIver , Mrs. Beatty , Mrs. Watson Coleman , and Ms. Brown ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend title 54, United States Code, to establish within the National Park Service the National Freedom Settlements Preservation Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Revitalizing and Empowering Freedom Settlements Through Opportunity, Resilience, and Education Act or the RESTORE Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAfter the Civil War, over 1,200 Freedmen\u2019s Settlements and Black Towns were established throughout the United States before and after emancipation, with at least 200 towns established by formerly enslaved individuals between 1866 and 1930, creating safe, self-sustaining, and thriving communities away from racial violence and economic discrimination.\n**(2)**\nFollowing the end of slavery, many African-American families who strived for land and housing security established their homes in Black Towns. These towns, founded and governed by recently-emancipated African-American people across the country, were known as Freedmen\u2019s Settlements, Freedom Colonies, or Black Towns.\n**(3)**\nAfrican Americans were often denied access to necessary public systems, such as education, housing, and neighborhood infrastructure. Across many areas of the United States, African-American people were barred from utilizing these services because of local segregating laws.\n**(4)**\nFreedmen\u2019s Settlements were established around the provision of community services, often structured around schools and churches, as Black residents came together to fulfill necessary resources they had been previously denied.\n**(5)**\nDespite these communities being an example of African-American communities\u2019 self-sufficiency amidst a discriminatory society, they were still terrorized by violent, White supremacist groups which initially excluded them from White systems.\n**(6)**\nDue to harsh circumstances which included violent attacks, exclusion from water and sanitation systems, as well as urban planning to remove Black Towns from railroads, many Freedmen\u2019s Settlements, which are predominantly in rural areas, are underdeveloped and lack accessibility due to many systemic challenges.\n**(7)**\nFreedmen\u2019s Settlements have been disproportionately impacted by economic and community underdevelopment, but have the potential to become thriving communities with proper support and investment that honors their rich history, meets the current needs of their residents, and uplifts community resilience and sustainable development.\n**(8)**\nMany of these Freedmen\u2019s Settlements and Black Towns were destroyed by southern domestic terrorists, or otherwise became impoverished by centuries of public and private divestment. This includes uncompensated enslaved labor, failed Reconstruction, and the unmet Freedmen\u2019s Bureau\u2019s postemancipation promises to transition people who were formerly enslaved into the American economy, Jim Crow laws, economic and housing discrimination through redlining, public housing, and transportation policies, and environmental racism. Some towns withstood systemic racism and racial violence, and serve as examples of community resilience.\n**(9)**\nIt is difficult to fully quantify and understand the history and current status of all the Freedmen\u2019s Settlements in the United States due to lack of research and investment in analyzing, preserving, and supporting these historic settlements, towns, and communities, with a large part of this history held by the descendants of the founders and residents.\n**(10)**\nA lack of accurate information is typical of African-American history following the Civil War, due to disenfranchisement of African Americans from predominantly White, institution-based documentation.\n**(11)**\nFreedmen\u2019s Settlements were often\u2014\n**(A)**\npoorly recorded;\n**(B)**\nexcluded from historical maps and databases;\n**(C)**\nrecognized only through oral traditions and community memory; and\n**(D)**\nsuffered from the negative consequences of systemic racism, such as the calculated exclusion from crucial infrastructure like water systems or railroads.\n**(12)**\nRecognizing and providing resources for Freedman\u2019s Settlements through Federal identification, designation of historic status, comprehensive documentation, funding, and physical commemoration would lead to greater equity and investment in historically disadvantaged communities that have faced centuries of racism, discrimination, environmental and climate injustices, and violence.\n**(13)**\nA handful of former Freedmen\u2019s Settlements have received State or local designation for their historic status, offering them an opportunity for preservation and public acknowledgment, such as the Freedmen\u2019s Town Historic District in Houston, Texas.\n**(14)**\nThere is an ongoing call, gaining much traction today, to preserve and document the history of Freedmen\u2019s Settlements, leading to projects such as the Texas Freedom Colonies Project, the Mapping Blackness Project, as well as the Freedmen\u2019s Bureau Search Portal created by the National Museum of African-American History and Culture, among others.\n**(15)**\nThe presence and location of historic Freedmen\u2019s Settlements should be recorded. There should be coordinated national, State, local, and Tribal efforts to preserve and restore Freedmen\u2019s Settlements.\n**(16)**\nFreedmen\u2019s Settlements are an integral component of the heritage of the United States, and their preservation and revitalization crucial for the communities themselves as well as a more complete understanding of American history and the ongoing struggle for racial equity. Establishing a program to recognize previously underserved Freedmen\u2019s Settlements would help communities identify and record these settlements, preserve local history, and better inform development decisions and community planning.\n**(17)**\nBy investing in the preservation of Freedom Settlements, which include Freedmen\u2019s Settlements, Freedom Colonies, and Black Towns, the United States has an opportunity to honor the legacy of self-determination and community-building that these settlements represent, while also creating models for sustainable, equitable community development that can inform broader efforts to address historical inequities and build stronger, more inclusive communities across the Nation.\n#### 3. National Freedom Settlements Preservation Program\nDivision B of subtitle III of title 54, United States Code, is amended by adding at the end the following:\n3092 National Freedom Settlements Preservation Program 309201. Definitions. 309202. Purpose. 309203. National Freedom Settlements Preservation Program. 309204. Authority to award grants. 309205. Freedom Settlements Study. 309206. Registry. 309207. Private Property Protection. 309208. Cooperative agreements and memoranda of understanding. 309209. Freedom Settlements Advisory Committee. 309201. Definitions In this chapter: (1) Advisory Committee The term Advisory Committee means the Freedom Settlements Advisory Committee established under section 309209. (2) Freedom Settlement The term Freedom Settlement means a community established by formerly enslaved African Americans following emancipation (also commonly referred to as \u2018Freedmen\u2019s Settlements\u2019, Freedom Colonies , or \u2018Black Towns\u2019). (3) Program The term Program means the National Freedom Settlements Preservation Program established under section 309204. (4) Study The term Study means the study required under section 309205. 309202. Purpose The purpose of this chapter is to\u2014 (1) recognize the importance of Freedom Settlements, including communities established by formerly enslaved people, free African Americans, and their descendants, the sacrifices made by those who used the Underground Railroad in search of freedom, equality, and material security, and the vision of Settlements founders; and (2) authorize the Secretary of the Interior to coordinate and facilitate Federal and non-Federal activities to identify, research, record, preserve, commemorate, honor, and interpret the history of Freedom Settlements, their significance as a crucial element in the evolution of African-American history, and their relevance in fostering the spirit of racial justice and wealth equality. 309203. National Freedom Settlements Preservation Program (a) In general The Secretary shall establish within the Service a program to be known as the National Freedom Settlements Preservation Program . (b) Duties of secretary In carrying out the Program, the Secretary shall develop a program for the provision of grants in accordance with section 309204(a), in consultation with\u2014 (1) organizations, experts, and community leaders who serve African-American communities; (2) organizations involved with Freedom Settlements; and (3) residents and descendants of residents of Freedom Settlements. (c) Donations The Secretary may accept donations of funds, services, or property for the purposes of carrying out this chapter. (d) Consent of private property owner required Freedom Settlements may only be considered for a grant under the Program\u2014 (1) with the consent of the owner of the applicable property; and (2) at the request of an individual, landowner, private or nonprofit organization, State, Tribal, or local government, or other entity. (e) Scope The Secretary may consider the following for inclusion in the Program: (1) All units and programs of the National Park Service determined by the Secretary to pertain to Freedom Settlements. (2) Historic properties pertaining to Freedom Settlements. (3) Other governmental and nongovernmental facilities and programs of an educational, research, or interpretive nature that are directly related to Freedom Settlements. 309204. Authority to award grants (a) In general In carrying out the Program, the Secretary may award grants to eligible entities described in subsection (b)(1) for\u2014 (1) the identification of Freedom Settlements that may qualify for the Program; (2) cultural and heritage preservation, restoration, and tourism program development of Freedom Settlements; (3) related research and documentation of Freedom Settlements; (4) capacity-building to operate and maintain recognized Freedom Settlement sites; and (5) educational programming about Freedom Settlement history. (b) Applications (1) Eligible entities Each of the following entities are eligible for a grant under the Program: (A) A property owner of a property associated with Freedom Settlements. (B) Tribal, State, or local governments. (C) Community organizations that have demonstrated local leadership and a commitment to community development. (2) Submission To be eligible for a grant under this section, an eligible entity shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require. (c) Authorization of appropriations There are authorized to be appropriated to the Secretary to carry out this section $3,000,000 for each of fiscal years 2026 through 2031. 309205. Freedom Settlements Study (a) Study The Secretary shall conduct a study to identify key sites that\u2014 (1) illustrate the period in American history when formerly enslaved African Americans established Freedom Settlements to provide their communities with education, security, and belonging which were previously denied under slavery and discriminatory laws; and (2) may be suitable for inclusion in the Program. (b) Consultation The Study shall be conducted with public involvement and in consultation with\u2014 (1) the Advisory Committee; (2) State and local officials; (3) educational institutions; and (4) other interested organizations and individuals. 309206. Registry The Secretary shall maintain and regularly update a comprehensive registry of Freedom Settlements, as they are identified and verified through the research and documentation process outlined in this chapter, including but not limited to historically documented settlements engaged in preservation efforts, such as\u2014 (1) Nicodemus, Kansas; (2) Africatown, Alabama; (3) Mound Bayou, Mississippi; (4) Eatonville, Florida; (5) Boley, Oklahoma; (6) Hobson City, Alabama; (7) Allensworth, California; (8) Freedmen\u2019s Town Historic District, Houston, Texas; (9) Independence Heights, Texas; (10) Mossville, Louisiana; (11) Oberlin Village, North Carolina; (12) Kinloch, Missouri; (13) New Philadelphia, Illinois; (14) Rosewood, Florida; (15) Weeksville, New York; (16) Freedman\u2019s Village, Arlington, Virginia; (17) Sandy Ground, New York; (18) Princeville, North Carolina; (19) Greenwood District (Black Wall Street), Tulsa, Oklahoma; and (20) Freedmen\u2019s Town, Dallas, Texas. 309207. Private Property Protection Nothing in this chapter\u2014 (1) authorizes the Secretary to require or affect the management or use of private property without the written consent of the owner of the private property; or (2) prohibits the Secretary from providing land management guidance or requirements relating to private property as a condition of a grant provided to the owner of the private property under this chapter. 309208. Cooperative agreements and memoranda of understanding The Secretary may enter into cooperative agreements and memoranda of understanding with, and provide technical assistance to, the heads of other Federal agencies, States, units of local government, Tribal governments, regional governmental bodies, African American-serving groups, residents and descendants of residents of Freedom Settlements, scholars of this specific history, and nonprofit organizations such as the Chisholm Legacy Project, Ubuntu Climate, and the Texas Freedom Colonies Project, educational institutions, and private entities\u2014 (1) to achieve the purposes of this chapter; (2) to facilitate cooperation with the Advisory Committee; and (3) to ensure effective coordination of the Federal elements and non-Federal elements provided a grant or other assistance under the Program with System units and programs of the Service. 309209. Freedom Settlements Advisory Committee (a) In general In carrying out the Study under section 309205, the Secretary shall establish a committee to be known as the Freedom Settlements Advisory Committee to assist with the Study. (b) Composition The Advisory Committee shall be composed of members, appointed by the Secretary, who\u2014 (1) are residents or descendants of residents of Freedom Settlements; (2) have demonstrated expertise in\u2014 (A) African-American history; or (B) Reconstruction or Jim Crow era history; or (3) are community leaders and advocates for African-American community heritage, preservation, and development. .",
      "versionDate": "2025-02-27",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advisory bodies",
            "updateDate": "2026-02-06T19:41:24Z"
          },
          {
            "name": "Alabama",
            "updateDate": "2026-02-06T19:40:26Z"
          },
          {
            "name": "California",
            "updateDate": "2026-02-06T19:40:43Z"
          },
          {
            "name": "Florida",
            "updateDate": "2026-02-06T19:40:35Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-02-06T19:40:16Z"
          },
          {
            "name": "Historic sites and heritage areas",
            "updateDate": "2026-02-06T19:40:10Z"
          },
          {
            "name": "Illinois",
            "updateDate": "2026-02-06T19:41:07Z"
          },
          {
            "name": "Kansas",
            "updateDate": "2026-02-06T19:40:21Z"
          },
          {
            "name": "Louisiana",
            "updateDate": "2026-02-06T19:40:52Z"
          },
          {
            "name": "Mississippi",
            "updateDate": "2026-02-06T19:40:31Z"
          },
          {
            "name": "Missouri",
            "updateDate": "2026-02-06T19:41:02Z"
          },
          {
            "name": "New York State",
            "updateDate": "2026-02-06T19:41:13Z"
          },
          {
            "name": "North Carolina",
            "updateDate": "2026-02-06T19:40:57Z"
          },
          {
            "name": "Oklahoma",
            "updateDate": "2026-02-06T19:40:39Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2026-02-06T19:39:54Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2026-02-06T19:39:59Z"
          },
          {
            "name": "Texas",
            "updateDate": "2026-02-06T19:40:47Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2026-02-06T19:40:06Z"
          },
          {
            "name": "Virginia",
            "updateDate": "2026-02-06T19:41:19Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-12T13:03:04Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1704ih.xml"
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
      "title": "RESTORE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-24T14:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RESTORE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T14:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Revitalizing and Empowering Freedom Settlements Through Opportunity, Resilience, and Education Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T14:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 54, United States Code, to establish within the National Park Service the National Freedom Settlements Preservation Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-24T14:03:37Z"
    }
  ]
}
```
