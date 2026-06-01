# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4310?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4310
- Title: Back the Blue Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4310
- Origin chamber: House
- Introduced date: 2025-07-10
- Update date: 2026-05-13T08:06:52Z
- Update date including text: 2026-05-13T08:06:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-10: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-07-10: Introduced in House

## Actions

- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4310",
    "number": "4310",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001298",
        "district": "2",
        "firstName": "Don",
        "fullName": "Rep. Bacon, Don [R-NE-2]",
        "lastName": "Bacon",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Back the Blue Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:52Z",
    "updateDateIncludingText": "2026-05-13T08:06:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-10",
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
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-10",
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
          "date": "2025-07-10T15:01:50Z",
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
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "ME"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "NJ"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4310ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4310\nIN THE HOUSE OF REPRESENTATIVES\nJuly 10, 2025 Mr. Bacon (for himself and Mr. Golden of Maine ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo protect law enforcement officers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Back the Blue Act of 2025 .\n#### 2. Protection of law enforcement officers\n##### (a) Killing of law enforcement officers\n**(1) Offense**\nChapter 51 of title 18, United States Code, is amended by adding at the end the following:\n1123. Killing of law enforcement officers (a) Definitions In this section\u2014 (1) the terms Federal law enforcement officer and United States judge have the meanings given those terms in section 115; (2) the term federally funded public safety officer means a public safety officer or judicial officer for a public agency that\u2014 (A) receives Federal financial assistance; and (B) is an agency of an entity that is a State of the United States, the District of Columbia, the Commonwealth of Puerto Rico, the Virgin Islands, Guam, American Samoa, the Commonwealth of the Northern Mariana Islands, or any territory or possession of the United States, an Indian tribe, or a unit of local government of that entity; (3) the term firefighter includes an individual serving as an official recognized or designated member of a legally organized volunteer fire department and an officially recognized or designated public employee member of a rescue squad or ambulance crew; (4) the term judicial officer means a judge or other officer or employee of a court, including prosecutors, court security, pretrial services officers, court reporters, and corrections, probation, and parole officers; (5) the term law enforcement officer means an individual, with statutory arrest powers, involved in crime or juvenile delinquency control or reduction or enforcement of the laws; (6) the term public agency includes a court system, the National Guard of a State to the extent the personnel of that National Guard are not in Federal service, and the defense forces of a State authorized by section 109 of title 32; and (7) the term public safety officer means an individual serving a public agency in an official capacity, as a law enforcement officer, as a firefighter, as a chaplain, or as a member of a rescue squad or ambulance crew. (b) Offense It shall be unlawful for any person to\u2014 (1) kill, or attempt or conspire to kill\u2014 (A) a United States judge; (B) a Federal law enforcement officer; or (C) a federally funded public safety officer while that officer is engaged in official duties, or on account of the performance of official duties; or (2) kill a former United States judge, Federal law enforcement officer, or federally funded public safety officer on account of the past performance of official duties. (c) Penalty Any person that violates subsection (b) shall be fined under this title and imprisoned for not less than 10 years or for life, or, if death results, shall be sentenced to not less than 30 years and not more than life, or may be punished by death. .\n**(2) Table of sections**\nThe table of sections for chapter 51 of title 18, United States Code, is amended by adding at the end the following:\n1123. Killing of law enforcement officers. .\n##### (b) Assault of law enforcement officers\n**(1) Offense**\nChapter 7 of title 18, United States Code, is amended by adding at the end the following:\n120. Assaults of law enforcement officers (a) Definition In this section, the term federally funded State or local law enforcement officer means an individual involved in crime and juvenile delinquency control or reduction, or enforcement of the laws (including a police, corrections, probation, or parole officer) who works for a public agency (that receives Federal financial assistance) of a State of the United States or the District of Columbia. (b) Offense It shall be unlawful to assault a federally funded State or local law enforcement officer while engaged in or on account of the performance of official duties, or assaults any person who formerly served as a federally funded State or local law enforcement officer on account of the performance of such person's official duties during such service, or because of the actual or perceived status of the person as a federally funded State or local law enforcement officer. (c) Penalty Any person that violates subsection (b) shall be subject to a fine under this title and\u2014 (1) if the assault resulted in bodily injury (as defined in section 1365), shall be imprisoned not less than 2 years and not more than 10 years; (2) if the assault resulted in substantial bodily injury (as defined in section 113), shall be imprisoned not less than 5 years and not more than 20 years; (3) if the assault resulted in serious bodily injury (as defined in section 1365), shall be imprisoned for not less than 10 years; (4) if a deadly or dangerous weapon was used during and in relation to the assault, shall be imprisoned for not less than 20 years; and (5) shall be imprisoned for not more than 1 year in any other case. (d) Certification requirement (1) In general No prosecution of any offense described in this section may be undertaken by the United States, except under the certification in writing of the Attorney General, or a designee, that\u2014 (A) the State does not have jurisdiction; (B) the State has requested that the Federal Government assume jurisdiction; (C) the verdict or sentence obtained pursuant to State charges left demonstratively unvindicated the Federal interest in eradicating bias-motivated violence; or (D) a prosecution by the United States is in the public interest and necessary to secure substantial justice. (2) Rule of construction Nothing in this subsection shall be construed to limit the authority of Federal officers, or a Federal grand jury, to investigate possible violations of this section. (e) Statute of limitations (1) Offenses not resulting in death Except as provided in paragraph (2), no person shall be prosecuted, tried, or punished for any offense under this section unless the indictment for such offense is found, or the information for such offense is instituted, not later than 7 years after the date on which the offense was committed. (2) Offenses resulting in death An indictment or information alleging that an offense under this section resulted in death may be found or instituted at any time without limitation. .\n**(2) Table of sections**\nThe table of sections for chapter 7 of title 18, United States Code, is amended by adding at the end the following:\n120. Assualts of law enforcement officers. .\n##### (c) Flight To avoid prosecution for killing law enforcement officials\n**(1) Offense**\nChapter 49 of title 18, United States Code, is amended by adding at the end the following:\n1075. Flight to avoid prosecution for killing law enforcement officials (a) Offense It shall be unlawful for any person to move or travel in interstate or foreign commerce with intent to avoid prosecution, or custody or confinement after conviction, under the laws of the place from which the person flees or under section 1114 or 1123, for a crime consisting of the killing, an attempted killing, or a conspiracy to kill a Federal judge or Federal law enforcement officer (as those terms are defined in section 115), or a federally funded public safety officer (as that term is defined in section 1123). (b) Penalty Any person that violates subsection (a) shall be fined under this title and imprisoned for not less than 10 years, in addition to any other term of imprisonment for any other offense relating to the conduct described in subsection (a). .\n**(2) Table of sections**\nThe table of sections for chapter 49 of title 18, United States Code, is amended by adding at the end the following:\n1075. Flight to avoid prosecution for killing law enforcement officials. .\n#### 3. Specific aggravating factor for Federal death penalty killing of law enforcement officer\n##### (a) Aggravating factors for homicide\nSection 3592(c) of title 18, United States Code, is amended by inserting after paragraph (16) the following:\n(17) Killing of a law enforcement officer, prosecutor, judge, or first responder The defendant killed or attempted to kill a person who is authorized by law\u2014 (A) to engage in or supervise the prevention, detention, or investigation of any criminal violation of law; (B) to arrest, prosecute, or adjudicate an individual for any criminal violation of law; or (C) to be a firefighter or other first responder. .\n#### 4. Limitation on Federal habeas relief for murders of law enforcement officers\n##### (a) Justice for law enforcement officers and their families\n**(1) In general**\nSection 2254 of title 28, United States Code, is amended by adding at the end the following:\n(j) (1) For an application for a writ of habeas corpus on behalf of a person in custody pursuant to the judgment of a State court for a crime that involved the killing of a public safety officer (as that term is defined in section 1204 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 42 U.S.C. 3796b )) or judge, while the public safety officer or judge was engaged in the performance of official duties, or on account of the performance of official duties by or status as a public safety officer or judge of the public safety officer or judge\u2014 (A) the application shall be subject to the time limitations and other requirements under sections 2263, 2264, and 2266; and (B) the court shall not consider claims relating to sentencing that were adjudicated in a State court. (2) Sections 2251, 2262, and 2101 are the exclusive sources of authority for Federal courts to stay a sentence of death entered by a State court in a case described in paragraph (1). .\n**(2) Rules**\nRule 11 of the Rules Governing Section 2254 Cases in the United States District Courts is amended by adding at the end the following: Rule 60(b)(6) of the Federal Rules of Civil Procedure shall not apply to a proceeding under these rules in a case that is described in section 2254(j) of title 28, United States Code. .\n**(3) Finality of determination**\nSection 2244(b)(3)(E) of title 28, United States Code, is amended by striking the subject of a petition and all that follows and inserting: reheard in the court of appeals or reviewed by writ of certiorari. .\n**(4) Effective date and applicability**\n**(A) In general**\nThis paragraph and the amendments made by this paragraph shall apply to any case pending on or after the date of enactment of this Act.\n**(B) Time limits**\nIn a case pending on the date of enactment of this Act, if the amendments made by this paragraph impose a time limit for taking certain action, the period of which began before the date of enactment of this Act, the period of such time limit shall begin on the date of enactment of this Act.\n**(C) Exception**\nThe amendments made by this paragraph shall not bar consideration under section 2266(b)(3)(B) of title 28, United States Code, of an amendment to an application for a writ of habeas corpus that is pending on the date of enactment of this Act, if the amendment to the petition was adjudicated by the court prior to the date of enactment of this Act.\n#### 5. Self-defense rights for law enforcement officers\n##### (a) In general\nChapter 203 of title 18, United States Code, is amended by inserting after section 3053 the following:\n3054. Authority of law enforcement officers to carry firearms Any sworn officer, agent, or employee of the United States, a State, or a political subdivision thereof, who is authorized by law to engage in or supervise the prevention, detection, investigation, or prosecution of any violation of law, or to supervise or secure the safety of incarcerated inmates, may carry firearms if authorized by law to do so. Such authority to carry firearms, with respect to the lawful performance of the official duties of a sworn officer, agent, or employee of a State or a political subdivision thereof, shall include possession incident to depositing a firearm within a secure firearms storage area for use by all persons who are authorized to carry a firearm within any building or structure classified as a Federal facility or Federal court facility, as those terms are defined under section 930, and any grounds appurtenant to such a facility. .\n##### (b) Carrying of concealed firearms by qualified law enforcement officers\nSection 926B(e)(2) of title 18, United States Code, is amended by inserting any magazine and after includes .\n##### (c) Carrying of concealed firearms by qualified retired law enforcement officers\nSection 926C(e)(1)(B) of title 18, United States Code, is amended by inserting any magazine and after includes .\n##### (d) School zones\nSection 922(q)(2)(B)(vi) of title 18, United States Code, is amended by inserting or a qualified law enforcement officer (as defined in section 926B(c)) before the semicolon.\n##### (e) Regulations required\nNot later than 60 days after the date of enactment of this Act, the Attorney General shall promulgate regulations allowing persons described in section 3054 of title 18, United States Code, to possess firearms in a manner described by that section. With respect to Federal justices, judges, bankruptcy judges, and magistrate judges, such regulations shall be prescribed after consultation with the Judicial Conference of the United States.\n##### (f) Table of sections\nThe table of sections for chapter 203 of title 18, United States Code, is amended by inserting after the item relating to section 3053 the following:\n3054. Authority of law enforcement officers to carry firearms. .\n##### (g) Further Amendment\nSection 930 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (2), by striking or at the end;\n**(B)**\nin paragraph (3), by striking the period at the end and inserting or ; and\n**(C)**\nby adding at the end the following:\n(4) the possession of a firearm or ammunition in a Facility Security Level I or II civilian public access facility by a qualified law enforcement officer (as defined in section 926B(c)) or a qualified retired law enforcement officer (as defined in section 926C(c)). ; and\n**(2)**\nin subsection (g), by adding at the end the following:\n(4) The term Facility Security Level means a security risk assessment level assigned to a Federal facility by the security agency of the facility in accordance with the biannually issued Interagency Security Committee Standard. (5) The term civilian public access facility means a facility open to the general public. .\n#### 6. Improving the relationship between law enforcement agencies and the communities they serve\n##### (a) In general\nFor each of fiscal years 2026 through 2030, the Attorney General using covered amounts shall, using such amounts as are necessary not to exceed $20,000,000, award grants to State, local, or tribal law enforcement agencies and appropriate nongovernmental organizations to\u2014\n**(1)**\npromote trust and ensure legitimacy among law enforcement agencies and the communities they serve through procedural reforms, transparency, and accountability;\n**(2)**\ndevelop comprehensive and responsive policies on key topics relevant to the relationship between law enforcement agencies and the communities they serve;\n**(3)**\nbalance the embrace of technology and digital communications with local needs, privacy, assessments, and monitoring;\n**(4)**\nencourage the implementation of policies that support community-based partnerships in the reduction of crime;\n**(5)**\nemphasize the importance of high quality and effective training and education through partnerships with local and national training facilities; and\n**(6)**\nendorse practices that support officer wellness and safety through the reevaluation of officer shift hours, including data collection and analysis.\n##### (b) Covered amounts defined\nIn this section, the term covered amounts means\u2014\n**(1)**\nany unobligated balances made available under the heading GENERAL ADMINISTRATION under the heading DEPARTMENT OF JUSTICE in an appropriations Act in a fiscal year;\n**(2)**\nany amounts made available for an Edward Byrne Memorial criminal justice innovation program under the heading STATE AND LOCAL LAW ENFORCEMENT ASSISTANCE under the heading OFFICE OF JUSTICE PROGRAMS under the heading DEPARTMENT OF JUSTICE in an appropriations Act in a fiscal year; or\n**(3)**\nany combination of amounts described in paragraphs (1) and (2).",
      "versionDate": "2025-07-10",
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
        "actionDate": "2025-12-04",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3366",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Back the Blue Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-09T14:18:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-10",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr4310",
          "measure-number": "4310",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-10",
          "originChamber": "HOUSE",
          "update-date": "2026-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4310v00",
            "update-date": "2026-04-24"
          },
          "action-date": "2025-07-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Back the Blue Act of 2025</strong></p><p>This bill establishes new criminal offenses for violent conduct against judicial officers and law enforcement officers and makes related changes. The bill also broadens the authority of certain law enforcement officers to carry firearms.\u00a0</p><p>With respect to new criminal offenses, the bill prohibits killing, attempting to kill, or conspiring to kill a federal judge, a federal law enforcement officer, or a public safety or judicial officer for a state, local, or tribal agency that receives federal funding. The bill also prohibits fleeing to avoid prosecution, custody, or confinement for such an offense.</p><p>Additionally, the bill prohibits killing former federal judges, former federal law enforcement officers, or former public safety or judicial officers for a state, local, or tribal agency that receives federal funding.</p><p>The bill also prohibits certain assaults on state or local law enforcement officers who work for an agency of a state or the District of Columbia that receives federal funding. \u00a0</p><p>The bill limits federal court review of challenges to state court convictions for killing a public safety officer or judge.</p><p>The bill allows federal, state, and local law enforcement officers to carry firearms if authorized by law. The bill also allows qualified law enforcement officers to carry concealed firearms and ammunition (including magazines) in school zones and in certain federal facilities that are open to the public.</p><p>Finally, the bill temporarily directs the Department of Justice to make grants\u00a0to improve relations between law enforcement agencies and the communities they serve.</p>"
        },
        "title": "Back the Blue Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4310.xml",
    "summary": {
      "actionDate": "2025-07-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Back the Blue Act of 2025</strong></p><p>This bill establishes new criminal offenses for violent conduct against judicial officers and law enforcement officers and makes related changes. The bill also broadens the authority of certain law enforcement officers to carry firearms.\u00a0</p><p>With respect to new criminal offenses, the bill prohibits killing, attempting to kill, or conspiring to kill a federal judge, a federal law enforcement officer, or a public safety or judicial officer for a state, local, or tribal agency that receives federal funding. The bill also prohibits fleeing to avoid prosecution, custody, or confinement for such an offense.</p><p>Additionally, the bill prohibits killing former federal judges, former federal law enforcement officers, or former public safety or judicial officers for a state, local, or tribal agency that receives federal funding.</p><p>The bill also prohibits certain assaults on state or local law enforcement officers who work for an agency of a state or the District of Columbia that receives federal funding. \u00a0</p><p>The bill limits federal court review of challenges to state court convictions for killing a public safety officer or judge.</p><p>The bill allows federal, state, and local law enforcement officers to carry firearms if authorized by law. The bill also allows qualified law enforcement officers to carry concealed firearms and ammunition (including magazines) in school zones and in certain federal facilities that are open to the public.</p><p>Finally, the bill temporarily directs the Department of Justice to make grants\u00a0to improve relations between law enforcement agencies and the communities they serve.</p>",
      "updateDate": "2026-04-24",
      "versionCode": "id119hr4310"
    },
    "title": "Back the Blue Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-07-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Back the Blue Act of 2025</strong></p><p>This bill establishes new criminal offenses for violent conduct against judicial officers and law enforcement officers and makes related changes. The bill also broadens the authority of certain law enforcement officers to carry firearms.\u00a0</p><p>With respect to new criminal offenses, the bill prohibits killing, attempting to kill, or conspiring to kill a federal judge, a federal law enforcement officer, or a public safety or judicial officer for a state, local, or tribal agency that receives federal funding. The bill also prohibits fleeing to avoid prosecution, custody, or confinement for such an offense.</p><p>Additionally, the bill prohibits killing former federal judges, former federal law enforcement officers, or former public safety or judicial officers for a state, local, or tribal agency that receives federal funding.</p><p>The bill also prohibits certain assaults on state or local law enforcement officers who work for an agency of a state or the District of Columbia that receives federal funding. \u00a0</p><p>The bill limits federal court review of challenges to state court convictions for killing a public safety officer or judge.</p><p>The bill allows federal, state, and local law enforcement officers to carry firearms if authorized by law. The bill also allows qualified law enforcement officers to carry concealed firearms and ammunition (including magazines) in school zones and in certain federal facilities that are open to the public.</p><p>Finally, the bill temporarily directs the Department of Justice to make grants\u00a0to improve relations between law enforcement agencies and the communities they serve.</p>",
      "updateDate": "2026-04-24",
      "versionCode": "id119hr4310"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4310ih.xml"
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
      "title": "Back the Blue Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T13:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Back the Blue Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T13:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To protect law enforcement officers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T13:48:30Z"
    }
  ]
}
```
