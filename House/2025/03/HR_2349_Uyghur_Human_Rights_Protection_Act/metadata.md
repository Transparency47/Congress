# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2349?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2349
- Title: Uyghur Human Rights Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 2349
- Origin chamber: House
- Introduced date: 2025-03-25
- Update date: 2025-10-01T08:05:51Z
- Update date including text: 2025-10-01T08:05:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-25 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-25: Introduced in House

## Actions

- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-25 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2349",
    "number": "2349",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001230",
        "district": "10",
        "firstName": "Suhas",
        "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
        "lastName": "Subramanyam",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Uyghur Human Rights Protection Act",
    "type": "HR",
    "updateDate": "2025-10-01T08:05:51Z",
    "updateDateIncludingText": "2025-10-01T08:05:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-25",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-25",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T14:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-25T14:03:05Z",
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
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NY"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "FL"
    },
    {
      "bioguideId": "C001078",
      "district": "11",
      "firstName": "Gerald",
      "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Connolly",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "VA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "HI"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "VA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "IA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "IN"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "RI"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NV"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "MA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "IL"
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
      "sponsorshipDate": "2025-04-01",
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
      "sponsorshipDate": "2025-04-01",
      "state": "NJ"
    },
    {
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "NJ"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "DC"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "DE"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "NY"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2349ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2349\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2025 Mr. Subramanyam (for himself, Mr. Meeks , Ms. Salazar , Mr. Connolly , Ms. Tokuda , Mr. Beyer , Mr. Sherman , Mr. Nunn of Iowa , Mr. Carson , Mr. Magaziner , Ms. Titus , Mr. Moulton , and Mr. Krishnamoorthi ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Foreign Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo designate residents of the Xinjiang Uyghur Autonomous Region as Priority 2 refugees of special humanitarian concern, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Uyghur Human Rights Protection Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nThe Government of the People\u2019s Republic of China has a long history of repressing Turkic Muslims and other Muslim minority groups, particularly Uyghurs, in the Xinjiang Uyghur Autonomous Region ( Xinjiang or XUAR ), also known as East Turkestan. Central and regional Chinese government policies have systematically discriminated against these minority groups by denying them a range of civil and political rights, particularly freedom of religion.\n**(2)**\nIn May 2014, the Government of the People's Republic of China launched its latest Strike Hard Against Violent Extremism campaign, using wide-scale, internationally linked threats of terrorism as a pretext to justify pervasive restrictions on and serious human rights violations against members of ethnic minority communities in Xinjiang. The August 2016 appointment of former Tibet Autonomous Region Party Secretary Chen Quanguo to be Party Secretary of the XUAR accelerated the crackdown across the region. Scholars, human rights organizations, journalists, and think tanks have provided ample evidence substantiating the establishment by the Government of the People's Republic of China of internment camps. Since 2017, the Government of the People's Republic of China has detained more than 1,000,000 Uyghurs, ethnic Kazakhs, Kyrgyz, and members of other Muslim minority groups in these camps. The total ethnic minority population of Xinjiang Uyghur Autonomous Region was approximately 13,000,000 at the time of the last census conducted by the People's Republic of China in 2010.\n**(3)**\nThe Government of the People's Republic of China's actions against Uyghurs, ethnic Kazakhs, Kyrgyz, and members of other Muslim minority groups in Xinjiang violate international human rights laws and norms, including\u2014\n**(A)**\nthe International Convention on the Elimination of All Forms of Racial Discrimination, to which the People's Republic of China has acceded;\n**(B)**\nthe Convention against Torture and Other Cruel, Inhuman or Degrading Treatment or Punishment, which the People's Republic of China has signed and ratified;\n**(C)**\nthe Convention on the Prevention and Punishment of the Crime of Genocide, which the People\u2019s Republic of China has signed and ratified;\n**(D)**\nthe International Covenant on Civil and Political Rights, which the People's Republic of China has signed; and\n**(E)**\nthe Universal Declaration of Human Rights and the International Labor Organization\u2019s Force Labor Convention (no. 29) and the Abolition of Forced Labor Convention (no. 105).\n**(4)**\nSenior Chinese Communist Party officials bear direct responsibility for gross human rights violations committed against Uyghurs, ethnic Kazakhs, Kyrgyz, and members of other Muslim minority groups. These abuses include the arbitrary detention of more than 1,000,000 Uyghurs, ethnic Kazakhs, Kyrgyz, and members of other Muslim minority groups, separation of working age adults from their children and elderly parents, and the integration of forced labor into supply chains.\n**(5)**\nThose held in detention facilities and internment camps in the Xinjiang Uyghur Autonomous Region have described forced political indoctrination, torture, beatings, food deprivation, sexual assault, coordinated campaigns to reduce birth rates among Uyghurs and other Turkic Muslims through forced sterilization, and denial of religious, cultural, and linguistic freedoms. These victims have confirmed they were told by guards that the only way to secure their release was to demonstrate adequate political loyalty. Poor conditions and lack of medical treatment at such facilities appear to have contributed to the deaths of some detainees, including the elderly and infirm. Recent media reports indicate that since 2019 the Government of the People\u2019s Republic of China has newly constructed, expanded, or fortified at least 60 detention facilities with higher security or prison-like features.\n**(6)**\nIn September 2018, United Nations High Commissioner for Human Rights Michelle Bachelet noted the deeply disturbing allegations of large-scale arbitrary detentions of Uyghurs and other Muslim communities, in so-called reeducation camps across Xinjiang .\n**(7)**\nIn 2019, the Congressional-Executive Commission on China concluded that, based on available evidence, the establishment and actions committed in the internment camps in Xinjiang Uyghur Autonomous Region may constitute crimes against humanity .\n**(8)**\nUyghurs and ethnic Kazaks resettled or residing in third countries report being subjected to threats and harassment from People\u2019s Republic of China officials.\n**(9)**\nThere is a backlog of approximately 3.6 million visa applicants waiting to enter the United States. Wait times for certain visas are between 5 and 18 years.\n#### 3. Designation of certain residents of the Xinjiang Uyghur Autonomous Region\n##### (a) In general\nPersons of special humanitarian concern eligible for Priority 2 processing under the refugee resettlement priority system shall include the following:\n**(1)**\nIndividuals who are residents of or fled the Xinjiang Uyghur Autonomous Region who suffered persecution or have a well-founded fear of persecution on account of their peaceful expression of political opinions, religious or cultural beliefs, or peaceful participation in political, religious, or cultural activities or associations.\n**(2)**\nIndividuals residing in other provinces of China, or individuals not firmly resettled in third countries, who fled the Xinjiang Uyghur Autonomous Region because of the causes described in paragraph (1).\n**(3)**\nIndividuals who have been formally charged, detained, or convicted on account of their peaceful actions as described in the Uyghur Human Rights Policy Act of 2020 ( Public Law 116\u2013145 ).\n**(4)**\nThe spouses, children, and parents (as such terms are defined in subsections (a) and (b) of section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 )) of individuals described in paragraph (1), (2), or (3), except such parents who are citizens of a country other than the People\u2019s Republic of China.\n##### (b) Processing of Xinjiang Uyghur Autonomous Region refugees\nThe processing of individuals described in subsection (a) for classification as refugees may occur in China or in a third country.\n##### (c) Eligibility for admission as refugees\nAn alien may not be denied the opportunity to apply for admission as a refugee under this section primarily because such alien\u2014\n**(1)**\nqualifies as an immediate relative of a citizen of the United States; or\n**(2)**\nis eligible for admission to the United States under any other immigrant classification.\n##### (d) Facilitation of admissions\nCertain applicants for admission to the United States from the Xinjiang Uyghur Autonomous Region, as described in subsection (a), may not be denied primarily on the basis of a politically, religiously, or culturally motivated arrest, detention, or other adverse government action taken against such applicant as a result of the participation by such applicant in protest activities.\n##### (e) Exclusion from numerical limitations\nAliens provided refugee status under this section shall not be counted against any numerical limitation under section 201, 202, 203, or 207 of the Immigration and Nationality Act ( 8 U.S.C. 1151 , 1152, 1153, or 1157).\n##### (f) Priority\nThe Secretary of State shall prioritize bilateral diplomacy with third countries hosting former residents from the Xinjiang Uyghur Autonomous Region, as described in subsection (a), and who face significant diplomatic pressure from the Government of the People\u2019s Republic of China.\n##### (g) Reporting requirements\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, and every 90 days thereafter, the Secretary of State and the Secretary of Homeland Security shall submit a report on the matters described in paragraph (2) to\u2014\n**(A)**\nthe Committee on the Judiciary and the Committee on Foreign Relations of the Senate; and\n**(B)**\nthe Committee on the Judiciary and the Committee on Foreign Affairs of the House of Representatives.\n**(2) Matters to be included**\nEach report required by paragraph (1) shall include\u2014\n**(A)**\nthe total number of applications that are pending at the end of the reporting period;\n**(B)**\nthe average wait times and number of applicants who are currently pending\u2014\n**(i)**\na pre-screening interview with a resettlement support center;\n**(ii)**\nan interview with U.S. Citizenship and Immigration Services;\n**(iii)**\nthe completion of security checks; and\n**(iv)**\nreceipt of a final decision after completion of an interview with U.S. Citizenship and Immigration Services; and\n**(C)**\nthe number of denials of applications for refugee status, disaggregated by the reason for each such denial.\n**(3) Form**\nEach report required by paragraph (1) shall be submitted in unclassified form, but may include a classified annex.\n**(4) Public reports**\nThe Secretary of State shall make each report submitted under this subsection available to the public on the internet website of the Department of State.\n##### (h) Satisfaction of other requirements\nAliens eligible under this section for Priority 2 processing under this section as Priority 2 refugees of special humanitarian concern under the refugee resettlement priority system shall be considered to satisfy the requirements under section 207 of the Immigration and Nationality Act ( 8 U.S.C. 1157 ) for admission to the United States.\n#### 4. Waiver of immigrant status presumption\n##### (a) In general\nThe presumption under the first sentence of section 214(b) of the Immigration and Nationality Act ( 8 U.S.C. 1184(b) ) that every alien is an immigrant until the alien establishes that the alien is entitled to nonimmigrant status shall not apply to an alien described in subsection (b).\n##### (b) Alien described\n**(1) In general**\nAn alien described in this paragraph is an alien who\u2014\n**(A)**\non January 1, 2023, was a resident of the Xinjiang Special Administrative Region;\n**(B)**\nfled the Xinjiang Special Administrative Region after June 30, 2009, and now resides in a different province of China or third country;\n**(C)**\nis seeking entry to the United States to apply for asylum under section 208 of the Immigration and Nationality Act ( 8 U.S.C. 1158 ); and\n**(D)**\nis facing repression in the Xinjiang Uyghur Autonomous Region by the Government of the People\u2019s Republic of China including\u2014\n**(i)**\nforced and arbitrary detention including in internment and so-called re-education camps;\n**(ii)**\nforced political indoctrination, torture, beatings, food deprivation, and denial of religious, cultural, and linguistic freedoms;\n**(iii)**\nforced labor;\n**(iv)**\nforced separation from family members; or\n**(v)**\nother forms of systemic threats, harassment, and gross human rights violations.\n**(2) Exclusion**\nAn alien described in this paragraph does not include any alien who\u2014\n**(A)**\nis a citizen or permanent resident of a country other than the People\u2019s Republic of China; or\n**(B)**\nis determined to have committed a gross violation of human rights.\n##### (c) Intention To abandon foreign residence\nThe fact that an alien described in this section is or was the beneficiary of an application for refugee status, or is seeking entry to the United States to apply for asylum under section 208 of the Immigration and Nationality Act ( 8 U.S.C. 1158 ), shall not constitute evidence of an intention to abandon a foreign residence for purposes of obtaining or maintaining the status of a nonimmigrant described in section 101(a)(15) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15) ).\n#### 5. Refugee and asylum determinations under the Immigration and Nationality Act\n##### (a) Persecution on account of political, religious, or cultural expression or association\n**(1) In general**\nIn the case of an alien who is within a category of aliens established under this Act, the alien may establish, for purposes of section 3(a)(1) of this Act, that the alien has a well-founded fear of persecution on account of race, religion, nationality, membership in a particular social group, or political opinion by asserting such a fear and asserting a credible basis for concern about the possibility of such persecution.\n**(2) Nationals of the People\u2019s Republic of China**\nFor purposes of refugee determinations under this Act in accordance with section 207 of the Immigration and Nationality Act ( 8 U.S.C. 1157 ), a national of the People\u2019s Republic of China whose residency in the Xinjiang Uyghur Autonomous Region, or any other area within the jurisdiction of the People\u2019s Republic of China, as determined by the Secretary of State, is revoked for having submitted to any United States Government agency a nonfrivolous application for refugee status, asylum, or any other immigration benefit under the immigration laws shall be considered to have suffered persecution on account of political opinion.\n##### (b) Changed circumstances\nFor purposes of asylum determinations under this Act in accordance with section 208 of the Immigration and Nationality Act ( 8 U.S.C. 1158 ), the revocation of the citizenship, nationality, or residency of an individual for having submitted to any United States Government agency a nonfrivolous application for refugee status, asylum, or any other immigration benefit under the immigration laws shall be considered to be a changed circumstance under subsection (a)(2)(D) of that section.\n##### (c) Definition\nFor purposes of this section, the term immigration laws has the meaning given such term in section 101(a)(17) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(17) ).\n#### 6. Statement of policy on encouraging allies and partners to make similar accommodations\nIt is the policy of the United States to encourage allies and partners of the United States to make accommodations similar to the accommodations made in this Act for residents of the Xinjiang Uyghur Autonomous Region who are fleeing oppression by the Government of the People\u2019s Republic of China.\n#### 7. Termination\nThis Act, and the amendments made by this Act, shall cease to have effect on the date that is 10 years after the date of the enactment of this Act.",
      "versionDate": "2025-03-25",
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
        "updateDate": "2025-04-04T16:42:29Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2349ih.xml"
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
      "title": "Uyghur Human Rights Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Uyghur Human Rights Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To designate residents of the Xinjiang Uyghur Autonomous Region as Priority 2 refugees of special humanitarian concern, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:45Z"
    }
  ]
}
```
