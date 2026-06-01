# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5573?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5573
- Title: Combatting Fentanyl Poisonings Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5573
- Origin chamber: House
- Introduced date: 2025-09-26
- Update date: 2026-02-10T09:05:31Z
- Update date including text: 2026-02-10T09:05:31Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5573",
    "number": "5573",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "E000300",
        "district": "8",
        "firstName": "Gabe",
        "fullName": "Rep. Evans, Gabe [R-CO-8]",
        "lastName": "Evans",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "Combatting Fentanyl Poisonings Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-10T09:05:31Z",
    "updateDateIncludingText": "2026-02-10T09:05:31Z"
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
          "date": "2025-09-26T14:05:45Z",
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
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "CA"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "CO"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "CO"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "TN"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "MS"
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
      "sponsorshipDate": "2025-10-17",
      "state": "VA"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "NY"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
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
      "bioguideId": "D000616",
      "district": "4",
      "firstName": "Scott",
      "fullName": "Rep. DesJarlais, Scott [R-TN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "DesJarlais",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5573ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5573\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Mr. Evans of Colorado (for himself, Mr. Gray , Ms. Boebert , Mr. Crank , Mr. Rose , and Mr. Guest ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to authorize grant programs to combat fentanyl poisonings.\n#### 1. Short title\nThis Act may be cited as the Combatting Fentanyl Poisonings Act of 2025 .\n#### 2. Grant programs to combat fentanyl poisonings\n##### (a) Grant programs authorized\nSubpart 1 of part E of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10151 et seq. ) is amended\u2014\n**(1)**\nby redesignating section 509 as section 510; and\n**(2)**\nby inserting after section 508 the following:\n509. Grant programs to combat fentanyl poisonings (a) Grants To prevent the sale of controlled substances on social media platforms (1) Authorization The Attorney General, acting through the Director of the Bureau of Justice Assistance, and in consultation with the Secretary of Health and Human Services, is authorized to award grants to State and local law enforcement agencies to assist such agencies in planning, designing, establishing, or operating locally based, proactive programs to combat the unlawful sale, marketing, or distribution of controlled substances (as such term is defined in section 102 of the Controlled Substance Act ( 21 U.S.C. 802 )) using social media platforms, including programs that\u2014 (A) prioritize the arrest of individuals who use social media platforms to unlawfully sell, market, or distribute controlled substances; and (B) provide education and training, including online training resources, to school personnel, clinicians, and the public in order to\u2014 (i) educate such persons on the dangers of ingesting controlled substances purchased using a social media platform, especially the risk of fentanyl poisoning from a counterfeit substance (as such term is defined in section 102 of the Controlled Substance Act ( 21 U.S.C. 802 )); and (ii) educate parents or personnel who are charged with the well-being and safety of children on commonly used methods of communication between online drug dealers and potential victims. (2) Application The head of a State or local law enforcement agency seeking a grant under this section shall submit to the Attorney General an application, at such time, in such manner, and containing such information as the Attorney General may reasonably require. (b) Grants To increase public awareness about the dangers of fentanyl (1) Authorization The Attorney General, acting through the Director of the Bureau of Justice Assistance, and in consultation with the Secretary of Health and Human Services, is authorized to award grants to non-profit organizations to assist such organizations in designing, establishing, and operating public education and awareness campaigns that teach individuals about the dangers of fentanyl. (2) Uses of funds Grants awarded under this section may be used for the following purposes: (A) Providing transportation for parents or immediate family members of individuals who died from fentanyl poisoning to speak at public events or awareness campaigns. (B) Creating, producing, and disseminating educational materials related to the dangers of fentanyl, such as documentaries, pamphlets, books, and infographics. (C) Providing counseling or mentorship services to individuals who have had a friend or a family member die from fentanyl poisoning. (D) Providing naloxone or overdose reversal education and training services to parents and school employees. (3) Limitation on uses of funds Grants awarded under this section may not be used to purchase harm reduction services or supplies, such as substance abuse test kits, sharps or medication disposal kits, medication lockboxes, supplies to promote sterile injection (including syringes and drug paraphernalia), safer smoking kits (including pipes, pipettes, and drug paraphernalia), and written educational materials on safer injection practices, except that such funds may be used to purchase naloxone, naloxone administration supplies, or naloxone administration training. (4) Maximum amount The maximum amount of a grant under this subsection is $50,000. (5) Definition In this subsection, the term nonprofit organization means an organization that is described in section 501(c)(3) of the Internal Revenue Code of 1986 and is exempt from taxation under section 501(a) of such Code. (c) Grants To protect law enforcement officers from fentanyl exposure (1) Authorization The Attorney General, acting through the Director of the Bureau of Justice Assistance, and in consultation with the Secretary of Health and Human Services, is authorized to award grants to State and local law enforcement agencies to assist such agencies in equipping and preparing law enforcement officers at risk of fentanyl exposure on duty. (2) Uses of funds Grants awarded under this section may be used for the following purposes: (A) Procuring and distributing equipment for fentanyl testing, fentanyl detection, and overdose reversal, including\u2014 (i) fentanyl test strips; (ii) field-portable ion mobility spectrometers; (iii) naloxone; and (iv) naloxone administration supplies; and (B) Providing training to officers on the use of equipment for fentanyl testing, fentanyl detection, and overdose reversal. .\n##### (b) Reserved funds\nSection 506(a) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10157(a) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking and at the end;\n**(2)**\nin paragraph (2), by striking the period at the end and inserting a semicolon; and\n**(3)**\nby adding at the end the following:\n(3) $10,000,000 for grants under section 509(a); (4) $3,000,000 for grants under section 509(b); and (5) $2,000,000 for grants under section 509(c). .",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-12-16T16:26:36Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5573ih.xml"
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
      "title": "Combatting Fentanyl Poisonings Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T07:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Combatting Fentanyl Poisonings Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T07:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Omnibus Crime Control and Safe Streets Act of 1968 to authorize grant programs to combat fentanyl poisonings.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T07:48:27Z"
    }
  ]
}
```
