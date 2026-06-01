# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7190?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7190
- Title: To end detention and electronic monitoring, and redirect funding to community-based wrap-around services.
- Congress: 119
- Bill type: HR
- Bill number: 7190
- Origin chamber: House
- Introduced date: 2026-01-21
- Update date: 2026-05-16T08:07:20Z
- Update date including text: 2026-05-16T08:07:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-21: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-21 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-22 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- 2026-01-22 - Committee: Referred to the Subcommittee on Oversight, Investigations, and Accountability.
- Latest action: 2026-01-21: Introduced in House

## Actions

- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-21 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-22 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- 2026-01-22 - Committee: Referred to the Subcommittee on Oversight, Investigations, and Accountability.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-21",
    "latestAction": {
      "actionDate": "2026-01-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7190",
    "number": "7190",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "R000617",
        "district": "3",
        "firstName": "Delia",
        "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
        "lastName": "Ramirez",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "To end detention and electronic monitoring, and redirect funding to community-based wrap-around services.",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:20Z",
    "updateDateIncludingText": "2026-05-16T08:07:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-22",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-22",
      "committees": {
        "item": {
          "name": "Oversight, Investigations, and Accountability Subcommittee",
          "systemCode": "hshm09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Oversight, Investigations, and Accountability.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-21",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-21",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-21",
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
          "date": "2026-01-21T15:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2026-01-22T21:02:32Z",
                "name": "Referred to"
              }
            },
            "name": "Border Security and Enforcement Subcommittee",
            "systemCode": "hshm11"
          },
          {
            "activities": {
              "item": {
                "date": "2026-01-22T21:02:32Z",
                "name": "Referred to"
              }
            },
            "name": "Oversight, Investigations, and Accountability Subcommittee",
            "systemCode": "hshm09"
          }
        ]
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-01-21T15:01:15Z",
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
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "NY"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "NY"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "IL"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "PA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "MI"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "AZ"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "AZ"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "IL"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "MN"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "TX"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "MA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7190ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7190\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2026 Mrs. Ramirez (for herself, Ms. Clarke of New York , Ms. Vel\u00e1zquez , Mr. Davis of Illinois , Ms. Lee of Pennsylvania , and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Homeland Security , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo end detention and electronic monitoring, and redirect funding to community-based wrap-around services.\n#### 1. Abolish immigration detention; repeal of detention authority and enforcement\n##### (a) Requirement for release on recognizance\nNot later than six months after the date of the enactment of this Act, the Secretary of Homeland Security shall release on their own recognizance any noncitizen detained by the Secretary of Homeland Security.\n##### (b) Repeal of detention authority and enforcement\n**(1) Inspection of applicants for admission**\nClauses (ii) and (iii)(IV) of section 235(b)(1)(B) of the Immigration and Nationality Act ( 8 U.S.C. 1225(b)(1)(B) ) are repealed.\n**(2) Inspection of other noncitizens**\nSubparagraphs (A), (B), and (C) of section 235(b)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1225(b)(2) ) are repealed.\n**(3) Authority relating to inspections**\nSection 235(d)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1225(d)(2) ) is amended\u2014\n**(A)**\nby striking subparagraphs (A) and (B); and\n**(B)**\nby striking United States\u2014 and inserting United States to deliver the noncitizen to an immigration officer for inspection or to a medical officer for examination. .\n**(4) Apprehension and detention of noncitizens**\nSection 236 of the Immigration and Nationality Act ( 8 U.S.C. 1226 ) is repealed.\n**(5) Detention and Removal of noncitizens ordered removed**\nSection 241 of the Immigration and Nationality Act ( 8 U.S.C. 1231 ) is amended\u2014\n**(A)**\nby striking subsection (a); and\n**(B)**\nby redesignating subsections (b), (c), (d), (e), (f), (g), and (h) as subsections (a), (b), (c), (d), (e), (f), (g), respectively.\n**(6) Power of immigration officers and employees**\nSection 287 of the Immigration and Nationality Act ( 8 U.S.C. 1357 ) is amended to read as follows:\n(a) Any officer or employee of the Service authorized under regulations prescribed by the Attorney General shall have power without warrant to arrest any alien who in his presence or view is entering or attempting to enter the United States in violation of any law or regulation made in pursuance of law regulating the admission, exclusion, expulsion or removal of aliens, or to arrest any alien in the United States, if he has reason to believe that the alien so arrested is in the United States in violation of any such law or regulation and is likely to escape before a warrant can be obtained for his arrest, but the alien arrested shall be taken without unnecessary delay for examination before an officer of the Service having authority to examine aliens as to their right to enter or remain in the United States. (b) An alien described in section 101(a)(27)(J) of the Immigration and Nationality Act who has been battered, abused, neglected, or abandoned, shall not be compelled to contact the alleged abuser (or family member of the alleged abuser) at any stage of applying for special immigrant juvenile status, including after a request for the consent of the Secretary of Homeland Security under section 101(a)(27)(J)(iii)(I) of such Act. .\n**(7) Authorizing State and local law enforcement officials to arrest and detain certain noncitizens**\nSection 439 of the Antiterrorism and Effective Death Penalty Act of 1996 ( 8 U.S.C. 1252C ) is repealed.\n**(8) Communication between State and local government agencies and the Immigration and Naturalization Service**\nSection 434 of the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 ( 8 U.S.C. 1644 ) is repealed.\n**(9) Communication between government agencies and the immigration and naturalization service**\nSection 642 of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1373 ) is repealed.\n**(10) Public charge; unlawful voters**\nParagraphs (5) and (6) of section 237(a) of the Immigration and Nationality Act ( 8 U.S.C. 1227 ) is repealed.\n##### (c) Termination of contracts for immigration detention\n**(1) Existing contracts with respect to physical detention and monitoring**\nNot later than two years after the date of the enactment of this Act, the Secretary of Homeland Security shall terminate any contract entered into by the Secretary of Homeland Security on or before the date of the enactment of this Act with respect to immigration detention and monitoring programs, including any contract with any entity that owns or operates a program or facility that provides services related to detention or monitoring.\n**(2) Other contracts with respect to physical detention and monitoring**\nBeginning on the date that is two years after the date of the enactment of this Act, no Federal funds may be used with respect to immigration detention and monitoring programs, including any contract with any entity that owns or operates a program or facility that provides services related to detention or monitoring.\n#### 2. Removal of enforcement authorities\n##### (a) Ankle monitoring system\n**(1) Plan required**\nNot later than one month after the date of the enactment of this Act, the Secretary of Homeland Security shall submit to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a plan to remove all ankle monitors from noncitizens being monitored by the Secretary.\n**(2) Removal of ankle monitors**\nNot later than six months after the date of the enactment of this Act, the Secretary of Homeland Security shall remove each ankle monitor from a noncitizen being monitored by the Secretary.\n**(3) Prohibition on use of Federal funds**\nBeginning on the date that is six months after the date of the enactment of this Act, no Federal funds may be used with respect to ankle monitors or ankle monitoring programs.\n##### (b) Secure communities program\nNot later than two years after the date of the enactment of this Act, no Federal funds may be used for information sharing partnerships between the Department of Homeland Security and any State or local law enforcement agency to identify or target noncitizens for the purpose of enforcing the immigration laws (as such term is defined in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 )).\n##### (c) Certain funds\nNone of the funds provided to U.S. Immigration and Customs Enforcement for Operations and Support may be used\u2014\n**(1)**\nto engage in civil immigration enforcement activities, including arrests, detention, removal, or the processing or issuance of charging documents;\n**(2)**\nto enforce, or assist another Federal, State, or local agency to enforce, a criminal offense in which an essential element of the offense is the noncitizen\u2019s immigration status, including State and local offenses and offenses under sections 243, 264, 275, or 276 or subsections (a) or (b) of section 266 of the Immigration and Nationality Act ( 8 U.S.C. 1253 ; 1304; 1325; 1326; 1306).\n#### 3. Grant program for wrap-around social services\n##### (a) Establishment\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Health and Human Services shall establish a grant program to award grants to an eligible entity to administer wrap-around social services to any individual affected by the enforcement of the immigration laws (as such term is defined under section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 )), including providing\u2014\n**(1)**\nhousing assistance;\n**(2)**\nmental health services;\n**(3)**\nassistance accessing healthcare;\n**(4)**\nfinancial empowerment and employment assistance;\n**(5)**\nEnglish classes;\n**(6)**\neducation assistance; and\n**(7)**\nimmigration legal assistance.\n##### (b) Eligible entity\nA grant awarded under this section shall be awarded to community-based non-profit organizations that are not involved, and have not previously been involved, in any immigration or law enforcement activity.\n##### (c) Provision of services\nAny services provided pursuant to a grant awarded under this section shall\u2014\n**(1)**\nbe provided on an opt-in and voluntary basis and shall not be made contingent on participation in any monitoring or compliance mechanisms; and\n**(2)**\nbe provided without subjecting individuals to surveillance or monitoring as they access such services, including physical, electronic, or other surveillance or monitoring.\n##### (d) Conditions on reporting\nA community-based organization providing services pursuant to a grant awarded under this section may not submit any personal identifying information relating to individuals to any Federal entity.",
      "versionDate": "2026-01-21",
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
        "updateDate": "2026-02-18T15:43:27Z"
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
      "date": "2026-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7190ih.xml"
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
      "title": "To end detention and electronic monitoring, and redirect funding to community-based wrap-around services.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T09:06:52Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To end detention and electronic monitoring, and redirect funding to community-based wrap-around services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-13T09:06:52Z"
    }
  ]
}
```
