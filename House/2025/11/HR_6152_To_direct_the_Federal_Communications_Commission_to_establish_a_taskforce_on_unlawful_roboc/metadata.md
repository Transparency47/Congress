# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6152?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6152
- Title: Foreign Robocall Elimination Act
- Congress: 119
- Bill type: HR
- Bill number: 6152
- Origin chamber: House
- Introduced date: 2025-11-19
- Update date: 2026-05-14T08:07:44Z
- Update date including text: 2026-05-14T08:07:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-11-19: Introduced in House

## Actions

- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6152",
    "number": "6152",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "M001240",
        "district": "6",
        "firstName": "Addison",
        "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
        "lastName": "McDowell",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Foreign Robocall Elimination Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:07:44Z",
    "updateDateIncludingText": "2026-05-14T08:07:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-19",
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
          "date": "2025-11-19T15:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "MN"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "FL"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NY"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "OK"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "TX"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-12-05",
      "state": "VA"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-12-05",
      "state": "TX"
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
      "sponsorshipDate": "2025-12-09",
      "state": "VA"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "NY"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "IL"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "CA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-12-23",
      "state": "NY"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "PA"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "NC"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "NC"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "NJ"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6152ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6152\nIN THE HOUSE OF REPRESENTATIVES\nNovember 19, 2025 Mr. McDowell (for himself, Ms. Morrison , Mr. Steube , and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Federal Communications Commission to establish a taskforce on unlawful robocalls, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Foreign Robocall Elimination Act .\n#### 2. Interagency taskforce on unlawful robocalls\n##### (a) Definitions\nIn this section:\n**(1) Commission**\nThe term Commission means the Federal Communications Commission.\n**(2) Consortium**\nThe term Consortium means the consortium described in section 13(d) of the Pallone-Thune TRACED Act ( Public Law 116\u2013105 ).\n**(3) Federal agency**\nThe term Federal agency has the meaning given the term agency in section 551 of title 5, United States Code.\n**(4) Taskforce**\nThe term taskforce means the taskforce on unlawful robocalls established under subsection (b).\n**(5) Unlawful robocall**\nThe term unlawful robocall means a telephone call made in violation of subsection (b) or (e) of section 227 of the Communications Act of 1934 ( 47 U.S.C. 227 ).\n##### (b) Establishment\nNot later than 270 days after the date of enactment of this Act, the Commission, after consultation with the Federal Trade Commission and the Attorney General, shall establish a taskforce on unlawful robocalls.\n##### (c) Membership\n**(1) In general**\nThe taskforce shall be composed of the following members:\n**(A)**\n**(i)**\nA representative of each Federal agency that the Chairman of the Commission, in consultation with the Chairman of the Federal Trade Commission and the Attorney General, considers appropriate.\n**(ii)**\nWith respect to each Federal agency considered under clause (i) to be appropriate, the Chairman of the Commission shall appoint a representative of that Federal agency to the taskforce based on the recommendations of the head of that Federal agency.\n**(B)**\nSeven representatives of private sector entities, to be appointed as described in paragraph (2)\u2014\n**(i)**\n3 of whom shall be representatives from private sector entities with expertise in combating unlawful robocalls, including\u2014\n**(I)**\nvoice service providers;\n**(II)**\nanalytics providers;\n**(III)**\ntechnologists; and\n**(IV)**\ntechnology experts;\n**(ii)**\n1 of whom shall be a representative from the Consortium;\n**(iii)**\n1 of whom shall be a representative of a marketing business that communicates with consumers by telephone as part of the normal course of business of that marketing business;\n**(iv)**\n1 of whom shall be a representative of a business or nonprofit organization that communicates with consumers by telephone for non-marketing purposes on a regular basis; and\n**(v)**\n1 of whom shall be a representative of an organization that advocates on behalf of customers and who has relevant experience and expertise in combating unlawful robocalls.\n**(2) Appointment of representatives of private sector entities**\n**(A) In general**\nNotwithstanding any provision of chapter 10 of title 5, United States Code, the members of the taskforce described in paragraph (1)(B) shall be jointly appointed by the Chairman of the Commission, the Chairman of the Federal Trade Commission, and the Attorney General.\n**(B) Inability to reach agreement**\n**(i) In general**\nSubject to clauses (ii) and (iii), if the Chairman of the Commission, the Chairman of the Federal Trade Commission, and the Attorney General cannot reach agreement regarding an appointment described in subparagraph (A), as determined by the Chairman of the Commission, the Chairman of the Commission shall make that appointment.\n**(ii) Notice of appointments**\nNot later than 48 hours before appointing a member to the taskforce under clause (i), the Chairman of the Commission shall provide notice of the proposed appointment to the commissioners of the Commission.\n**(iii) Request for vote**\nIf, after receiving notice under clause (ii) of a proposed appointment under clause (i), a commissioner of the Commission requests that the proposed appointment be subject to a vote of the Commission, the Chairman of the Commission may not make that appointment unless a majority of the commissioners of the Commission vote to approve the appointment.\n##### (d) Report\n**(1) In general**\nThe taskforce shall prepare a report on unlawful robocalls, which shall contain recommendations and advice for Federal agencies with jurisdiction relevant to combating unlawful robocalls, and for Congress, regarding the most effective ways to combat unlawful robocalls made into the United States from outside the United States.\n**(2) Matters to be studied**\nIn preparing the report required under paragraph (1), the taskforce shall\u2014\n**(A)**\ncompare the estimated number of suspected unlawful robocalls made within the United States with the estimated number of unlawful robocalls made into the United States from outside the United States;\n**(B)**\ndetermine which foreign countries serve as the foreign points of departure for the highest volume of unlawful robocalls made into the United States;\n**(C)**\ndetermine the magnitude of financial loss and the number of instances of stolen identity that occur within the United States each year as a result of unlawful robocalls made from outside the United States;\n**(D)**\nexamine methods for encouraging the adoption of caller identification authentication technology in foreign countries;\n**(E)**\nexamine and provide information on options for how countries can collaborate on solutions to authenticate and verify international calls, including relevant analytics relating to unlawful robocalls and technical options that can be used with respect to that authentication and verification;\n**(F)**\nexamine how better implementation of technical solutions, such as traceback and caller identification authentication technology in foreign originating countries, would improve coordination between the United States and foreign countries in combating unlawful robocalls;\n**(G)**\ndetermine whether\u2014\n**(i)**\nthe technical standards commonly known as STIR/SHAKEN adequately provide call authentication for unlawful robocalls from foreign originating providers or foreign intermediate providers through gateway providers in the United States; and\n**(ii)**\nit would be desirable to encourage other countries to adopt the standards described in clause (i);\n**(H)**\nexamine ways to provide incentives to foreign countries to cooperate with law enforcement efforts in the United States to combat unlawful robocalls;\n**(I)**\nexamine whether any Federal agency, or any other organization, that combats unlawful robocalls needs additional resources in order to more effectively combat unlawful robocalls made into the United States from outside the United States;\n**(J)**\nspecifically consider whether the ability of the Attorney General to conduct enforcement activities with respect to unlawful robocalls would be increased through the establishment of an office within the Department of Justice dedicated to those enforcement activities;\n**(K)**\nexamine how increased criminal penalties based on the volume of unlawful robocalls could help prevent unlawful robocalls made into the United States;\n**(L)**\nexamine how many enforcement activities the Attorney General has undertaken in the year preceding the date on which the preparation of the report begins, including in response to referrals made by the Commission;\n**(M)**\nspecifically determine how the Attorney General has pursued forfeiture amounts in enforcement activities with respect to unlawful robocalls;\n**(N)**\nseek input, as appropriate, from technologists and private sector innovators to find solutions for combating unlawful robocalls;\n**(O)**\nidentify a list of best practices regarding the identification and blocking of unlawful robocalls that telephone service providers and providers of technology solutions can voluntarily implement to improve the effectiveness of mitigating unlawful robocalls made into the United States from outside the United States;\n**(P)**\nevaluate whether requiring periodic public disclosure, in whole or in part, of the results of trace backs conducted by the Consortium would impact the integrity and effectiveness of the trace back process of the Consortium, including by\u2014\n**(i)**\nrevealing investigative methods;\n**(ii)**\nallowing consumers and businesses to avoid providers with a track record of making unlawful robocalls;\n**(iii)**\nexposing proprietary, competitively sensitive, or confidential information of legitimate providers or entities;\n**(iv)**\nstrengthening accountability and deterrence;\n**(v)**\nenabling the initiators of unlawful robocalls to evade detection, adapt tactics, or exploit system vulnerabilities;\n**(vi)**\nimproving the efforts of voice service providers to block calls that are determined to be unwanted based on reasonable analytics;\n**(vii)**\nimpeding cooperation with future law enforcement investigations or future consumer protection efforts; or\n**(viii)**\nensuring fairness in the reporting of trace back information; and\n**(Q)**\nexamine mechanisms for improving compliance with the requirements imposed pursuant to sections 6 and 7 of the Pallone-Thune TRACED Act ( 47 U.S.C. 227b\u20131 , 227 note).\n**(3) Report to Congress**\nNot later than 360 days after the date on which the taskforce is established under subsection (b), the taskforce shall submit to Congress the report prepared under this subsection.\n##### (e) Use of funds\nNotwithstanding section 1346 of title 31, United States Code, funds made available by this or any other Act to the Commission, the Federal Trade Commission, or the Department of Justice may be used by the applicable Federal agency for coordination with, participation in, or recommendations involving the taskforce, as required under this section.\n##### (f) Termination\nThe taskforce shall terminate on the date that is 90 days after the date on which the taskforce submits to Congress the report prepared under subsection (d), as required under paragraph (3) of that subsection.\n#### 3. FCC notice provision\nSection 13(d)(2) of the Pallone-Thune TRACED Act ( Public Law 116\u2013105 ) is amended by striking annually and inserting once every 3 years .\n#### 4. Robocall Mitigation Database\n##### (a) Definitions\nIn this section:\n**(1) Commission**\nThe term Commission means the Federal Communications Commission.\n**(2) Robocall Mitigation Database**\nThe term Robocall Mitigation Database has the meaning given the term in section 64.6300 of title 47, Code of Federal Regulations, or any successor regulation.\n**(3) Unlawful robocall**\nThe term unlawful robocall has the meaning given the term in section 2(a).\n##### (b) Bond requirement\n**(1) In general**\nThe Commission shall issue rules to require that, subject to the other provisions of this section, before a provider may file a certification to the Robocall Mitigation Database, the provider shall post a bond in an amount that is not more than $100,000, if the Commission determines that posting such a bond is necessary to preserve the integrity of the Robocall Mitigation Database.\n**(2) Excepted providers**\n**(A) In general**\nIn issuing rules under paragraph (1), the Commission shall establish criteria to exempt a provider from the requirement to post a bond described in that paragraph if that requirement, as applied to the provider, is not necessary to deter unlawful robocall activity.\n**(B) Considerations**\nIn establishing criteria under subparagraph (A), the Commission shall require consideration of whether a provider\u2014\n**(i)**\nis registered with the Commission under section 64.1195 of title 47, Code of Federal Regulations (or any successor regulation) and makes contributions under section 254(d) of the Communications Act of 1934 ( 47 U.S.C. 254(d) );\n**(ii)**\nholds a certificate of authority, license, or registration with a State public utility commission;\n**(iii)**\nis an issuer, the securities of which are listed on a national securities exchange; and\n**(iv)**\notherwise presents indicia of being a bona fide, established communications service provider, such that requiring the provider to post a bond under paragraph (1) would impose unnecessary burdens without materially improving enforcement of section 227 of the Communications Act of 1934 ( 47 U.S.C. 227 ).\n##### (c) Implementation\nIn implementing this section, the Commission shall\u2014\n**(1)**\nrequire the posting of a bond under subsection (b)(1) from providers that do not demonstrate\u2014\n**(A)**\nlegitimate, ongoing operations;\n**(B)**\nregulatory oversight sufficient to ensure accountability; or\n**(C)**\nthe ability to pay fines or forfeitures imposed by the Commission or other governmental enforcement authorities with respect to violations of Federal or State laws or regulations;\n**(2)**\nestablish categorical exemptions for identifiable classes of legitimate providers that satisfy the criteria established under subsection (b)(2); and\n**(3)**\nminimize administrative and financial burdens on compliant, established, and regulated providers while ensuring effective enforcement of section 227 of the Communications Act of 1934 ( 47 U.S.C. 227 ).\n#### 5. Registered consortium conducting private-led efforts to trace back the origin of suspected unlawful robocalls\n##### (a) Immunity for receiving, sharing, and publishing trace back information\nSection 13(d) of the Pallone-Thune TRACED Act ( Public Law 116\u2013105 ; 133 Stat. 3287) is amended by adding at the end the following:\n(3) Immunity for receiving, sharing, and publishing trace back information (A) Definition In this paragraph, the term covered information \u2014 (i) means information regarding suspected\u2014 (I) fraudulent, abusive, or unlawful robocalls; (II) illegally spoofed calls; and (III) other illegal calls; and (ii) includes\u2014 (I) call detail records of calls described in clause (i); (II) the names of, and other identifying information concerning, the voice service providers that originated, carried, routed, and transmitted calls described in clause (i); and (III) information about the entities that made calls described in clause (i), including any contact information of individuals that such an entity provided to the voice service provider that originated the call. (B) Trace back immunity No cause of action shall lie or be maintained in any court against the registered consortium for receiving, sharing, or publishing covered information or information derived from covered information. .\n##### (b) Publication of list of voice service providers\nSection 13(e) of the Pallone-Thune TRACED Act ( Public Law 116\u2013105 ; 133 Stat. 3288) is amended to read as follows:\n(e) List of voice service providers (1) Publication of list The Commission, or the registered consortium in consultation with the Commission, may publish a list of voice service providers based on\u2014 (A) information obtained by the consortium about voice service providers that refuse to participate in private-led efforts to trace back the origin of suspected unlawful robocalls; and (B) other information the Commission or the consortium may collect about voice service providers that are found to originate or transmit substantial amounts of unlawful robocalls. (2) Enforcement The Commission may take enforcement action based on the information described in paragraph (1). .",
      "versionDate": "2025-11-19",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-12-02T15:33:51Z"
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
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6152ih.xml"
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
      "title": "Foreign Robocall Elimination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-27T01:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Foreign Robocall Elimination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-27T01:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Federal Communications Commission to establish a taskforce on unlawful robocalls, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-27T01:48:20Z"
    }
  ]
}
```
