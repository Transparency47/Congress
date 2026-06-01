# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4817?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4817
- Title: Immigrant Witness and Victim Protection Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4817
- Origin chamber: House
- Introduced date: 2025-07-29
- Update date: 2025-09-17T17:03:07Z
- Update date including text: 2025-09-17T17:03:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-07-29: Introduced in House

## Actions

- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4817",
    "number": "4817",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "P000613",
        "district": "19",
        "firstName": "Jimmy",
        "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
        "lastName": "Panetta",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Immigrant Witness and Victim Protection Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-17T17:03:07Z",
    "updateDateIncludingText": "2025-09-17T17:03:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-29",
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
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T21:01:40Z",
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
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4817ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4817\nIN THE HOUSE OF REPRESENTATIVES\nJuly 29, 2025 Mr. Panetta (for himself and Ms. Moore of Wisconsin ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to eliminate the annual numerical limitation on visas for certain immigrants, to require the Secretary of Homeland Security to grant work authorization to certain immigrants with a pending application for nonimmigrant status under such Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Immigrant Witness and Victim Protection Act of 2025 .\n#### 2. Purpose; Findings; Sense of Congress\n##### (a) Purpose\nThe purpose of this Act is to remove barriers for alien survivors of domestic violence, sexual assault, human trafficking, and other crimes who may be eligible for protections under the Violence Against Women Act of 1994 (VAWA), the Trafficking Victims Protection Act of 2000 (TVPA), and their subsequent reauthorizations.\n##### (b) Findings\nCongress finds the following:\n**(1)**\nThreats of deportation are one of the most potent tools abusers and perpetrators of crime use to maintain control over and silence alien victims and to avoid criminal prosecution. Abusers and perpetrators leverage the immigration system in the abuse and exploitation of aliens they victimize.\n**(2)**\nA bipartisan majority in Congress created critical immigration protections in VAWA, TVPA and their subsequent reauthorizations in recognition that alien survivors of domestic violence, sexual assault, human trafficking, and other eligible crimes often fear that reaching out for help may lead to their deportation.\n**(3)**\nDetention and removal of those with victim-based cases undermines the intent of VAWA, TVPA, and their subsequent reuauthorizations and re-traumatizes victims and their children. Deporting survivors while they await decisions on their cases discourages victims from accessing justice, undermines the usefulness of these forms of relief as tools for law enforcement that seek to keep all communities safe, separates them from their children and support networks, and eliminates the ability of local law enforcement to continue protecting and working with such crime survivors.\n**(4)**\nLack of timely access to employment authorization makes victims more vulnerable and may lead to their need to endure or return to abusive relationships or exploitative conditions. Crime and abuse survivors should have access to work authorization to escape abusive situations, and gain self-sufficiency following victimization so they can support themselves and their families.\n##### (c) Sense of Congress\nIt is the sense of Congress that the Secretary of Homeland Security should not deport crime victims or neglected, abused, or abandoned youth before their applications for humanitarian relief are fully adjudicated, as it undermines critical bipartisan protections created in VAWA, TVPA, and their subsequent reauthorizations.\n#### 3. Elimination of annual numerical limitation on U visas\nSection 214(p) of the Immigration and Nationality Act ( 8 U.S.C. 1184(p) ) is amended by striking paragraph (2).\n#### 4. Elimination of annual numerical limitation on special immigrant juvenile visas\n##### (a) Aliens not subject To direct numerical limitations\nSection 201(b)(1)(A) of the Immigration and Nationality Act ( 8 U.S.C. 1151(b)(1)(A) ) is amended by striking subparagraph (A) or (B) and inserting subparagraphs (A), (B), or (J) .\n##### (b) Per country levels\nSection 202(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1152(a)(2) ) is amended by striking (5), and inserting (5), and except for special immigrants described in subparagraph (J) of section 1101(a)(27) of this title, .\n##### (c) Certain special immigrants\nSection 203(b)(4) of the Immigration and Nationality Act ( 8 U.S.C. 1153(b)(4) ) is amended by striking subparagraph (A) or (B) and inserting subparagraphs (A), (B), or (J) .\n#### 5. Work authorization while applications and petitions are pending\n##### (a) U visas\nSection 214(p) of the Immigration and Nationality Act ( 8 U.S.C. 1184(p) ) is amended\u2014\n**(1)**\nin paragraph (6), by striking the last sentence; and\n**(2)**\nby adding at the end the following:\n(8) Work authorization Notwithstanding any provision of this Act granting eligibility for employment in the United States, the Secretary of Homeland Security shall grant employment authorization to an alien who has filed an application for nonimmigrant status under section 101(a)(15)(U) on the date that is the earlier of\u2014 (A) the date on which the alien\u2019s application for such status is approved; or (B) a date determined by the Secretary that is not later than 180 days after the date on which the alien filed the application. .\n##### (b) T visas\nSection 214(o) of the Immigration and Nationality Act ( 8 U.S.C. 1184(o) ) is amended by adding at the end the following:\n(8) Notwithstanding any provision of this Act granting eligibility for employment in the United States, the Secretary of Homeland Security shall grant employment authorization to an alien who has filed a petition for nonimmigrant status under section 101(a)(15)(T) on the date that is the earlier of\u2014 (A) the date on which the alien\u2019s petition for such status is approved; or (B) a date determined by the Secretary that is not later than 180 days after the date on which the alien filed the petition. .\n##### (c) VAWA Self-Petitioners\nSection 204(a)(1)(K) of the Immigration and Nationality Act ( 8 U.S.C. 1154(a)(1)(K) ) is amended to read:\n(K) Notwithstanding any provision of this Act restricting eligibility for employment in the United States, the Secretary of Homeland Security shall grant employment authorization to such an alien in the United States on the date that is the earlier of\u2014 (i) the date on which the alien\u2019s petition as a VAWA self-petitioner is approved; or (ii) a date determined by the Secretary that is not later than 180 days after the date on which the alien filed the petition as a VAWA self-petitioner. .\n##### (d) Special immigrant juveniles\nSection 245 of the Immigration and Nationality Act ( 8 U.S.C. 1255 ) is amended by adding at the end the following:\n(o) Work authorization for certain special immigrants Notwithstanding any provision of this Act granting eligibility for employment in the United States, the Secretary of Homeland Security shall grant employment authorization to an alien who has filed a petition for special immigrant status under section 101(a)(27)(J) on the date that is the earlier of\u2014 (1) the date on which the alien\u2019s petition for such status is approved; or (2) a date determined by the Secretary that is not later than 180 days after the date on which the alien filed the petition. .\n##### (e) Cancellation of removal\nSection 240A(b)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1229b(b)(2) ) is amended by adding at the end the following:\n(E) Work authorization Notwithstanding any provision of this Act granting eligibility for employment in the United States, the Secretary of Homeland Security shall grant employment authorization to an alien who has filed an application for cancellation of removal under this paragraph on a date that is not later than 180 days after the date on which the alien filed the application. .\n#### 6. Stay of removal\n##### (a) In general\nAn alien described in subsection (b) shall not be removed from the United States under section 240 of the Immigration and Nationality Act ( 8 U.S.C. 1229a ) or any other provision of law until there is a final denial of the alien\u2019s application for status after the exhaustion of administrative and judicial review.\n##### (b) Aliens described\nAn alien is described in this subsection if the alien\u2014\n**(1)**\nhas a pending or approved application or petition under section 101(a)(15)(T), 101(a)(15)(U), 101(a)(27)(J), 106, 240A(b)(2), or 244(a)(3) (as in effect on March 31, 1997) of the Immigration and Nationality Act ( 8 U.S.C. 1101 , 1229a, 1254a); or\n**(2)**\nis a VAWA self-petitioner, as defined in section 101(a)(51) of the Immigration and Nationality Act, with a pending application for relief under a provision referred to in one of subparagraphs (A) through (G) of such section.\n#### 7. Prohibition on detention of certain victims with pending or approved petition or application\nSection 236 of the Immigration and Nationality Act ( 8 U.S.C. 1226 ) is amended by adding at the end the following:\n(f) Prohibition on detention of certain victims with pending or approved petitions and applications (1) In general Notwithstanding any other provision of this Act, there shall be a presumption that the alien described in paragraph (2) should be released from detention. The Secretary of Homeland Security shall have the duty of rebutting this presumption, which may only be shown based on clear and convincing evidence, including credible and individualized information, that the use of alternatives to detention will not reasonably ensure the appearance of the alien at removal proceedings, or that the alien is a threat to another person or the community. The fact that an alien has a criminal charge pending against the alien may not be the sole factor to justify the continued detention of the alien. (2) Alien described An alien is described in this paragraph if the alien\u2014 (A) has a pending or approved application or petition under section 101(a)(15)(T), 101(a)(15)(U), 101(a)(27)(J), 106, 240A(b)(2), or 244(a)(3) (as in effect on March 31, 1997); or (B) is a VAWA self-petitioner, as defined in section 101(a)(51), with a pending application for relief under a provision referred to in one of subparagraphs (A) through (G) of such section. .\n#### 8. Penalties for disclosure of information\n##### (a) In general\nSection 384 of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1367 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), by striking solely ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby striking information which relates and inserting information, files, or records which relate ; and\n**(ii)**\nby striking the period at the end and inserting a semicolon; and\n**(C)**\nby inserting after paragraph (2) the following new paragraph:\n(3) Except as provided in this paragraph, neither the Department, nor any other official or employee of the Department, or bureau or agency thereof, nor the Department of Justice, nor any official or employee of the Department of Justice, or bureau or agency thereof, may\u2014 (A) use the information furnished by the applicant pursuant to an application filed under paragraph (15)(T), (15)(U), (27)(J), or (51) of section 101(a) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a) (15)(T), (15)(U), (27)(J), or (51)), or section 240A(b)(2) of such Act ( 8 U.S.C. 1229b(b)(2) ), section 106 ( 8 U.S.C. 1105a ), for any purpose other than to make a determination on the application, or for enforcement of subsection (c) of this section; (B) make any publication of information that identifies a particular individual; or (C) permit anyone other than the sworn officers and employees of the Department or bureau or agency to examine individual applications. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (2), by striking legitimate law enforcement purpose, and inserting a criminal investigation or prosecution, ; and\n**(B)**\nby striking paragraph (4) and inserting the following new paragraph:\n(4) Paragraphs (2) and (3) of subsection (a) shall not apply if all the individuals in the case are adults and they have all waived the restrictions of such subsections. ; and\n**(3)**\nin subsection (d), by adding at the end the following: The Attorney General, Secretary of State, and the Secretary of Homeland Security shall provide Congress with an annual report regarding training provided to officers and employees, the number of investigations opened for violations of paragraphs (1) through (3) of subsection (a), and the results of those investigations. .",
      "versionDate": "2025-07-29",
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
        "updateDate": "2025-09-17T17:03:07Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4817ih.xml"
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
      "title": "Immigrant Witness and Victim Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Immigrant Witness and Victim Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to eliminate the annual numerical limitation on visas for certain immigrants, to require the Secretary of Homeland Security to grant work authorization to certain immigrants with a pending application for nonimmigrant status under such Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:33:26Z"
    }
  ]
}
```
