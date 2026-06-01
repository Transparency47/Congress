# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2406?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2406
- Title: National Oceanic and Atmospheric Administration Sexual Harassment and Assault Prevention Improvements Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2406
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2026-05-30T08:05:46Z
- Update date including text: 2026-05-30T08:05:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-05-29 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-05-29 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2406",
    "number": "2406",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "B001278",
        "district": "1",
        "firstName": "Suzanne",
        "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
        "lastName": "Bonamici",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "National Oceanic and Atmospheric Administration Sexual Harassment and Assault Prevention Improvements Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:46Z",
    "updateDateIncludingText": "2026-05-30T08:05:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-29",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water, Wildlife and Fisheries.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:04:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-05-29T21:00:00Z",
              "name": "Referred to"
            }
          },
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
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
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "FL"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-31",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2406ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2406\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Ms. Bonamici (for herself, Ms. Salazar , and Mr. Huffman ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the National Defense Authorization Act for Fiscal Year 2017 to address sexual harassment and sexual assault involving National Oceanic and Atmospheric Administration personnel, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the National Oceanic and Atmospheric Administration Sexual Harassment and Assault Prevention Improvements Act of 2025 .\n#### 2. References\nExcept as otherwise specifically provided, whenever in this Act an amendment or repeal is expressed in terms of an amendment to, or repeal of, a provision, the reference shall be considered to be made to a provision of subtitle C of title XXXV of the National Defense Authorization Act for Fiscal Year 2017 ( 33 U.S.C. 894 et seq. ).\n#### 3. Policy on prevention of and response to sexual harassment involving National Oceanic and Atmospheric Administration personnel\nSection 3541(f) ( 33 U.S.C. 894(f) ) is amended\u2014\n**(1)**\nby inserting and equal employment after sexual harassment in each place it appears; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby redesignating subparagraphs (C) and (D) as subparagraphs (D) and (E), respectively; and\n**(B)**\nby inserting after subparagraph (B) the following:\n(C) Relevant data, including\u2014 (i) a synopsis of each case and the disciplinary action taken, if any, with respect to each such case; and (ii) data collected pursuant to the Notification and Federal Employee Antidiscrimination and Retaliation Act of 2002 ( 5 U.S.C. 2301 note). .\n#### 4. Annual report on sexual harassment, sexual assault, and equal employment\nSection 3548 ( 33 U.S.C. 894e ) is amended\u2014\n**(1)**\nby striking the section heading and inserting the Annual report on sexual harassment, sexual assault, and equal employment in National Oceanic and Atmospheric Administration .\n**(2)**\nin subsection (a), by striking the sexual assaults involving and inserting sexual harassment and sexual assault cases involving, and the equal employment of, ;\n**(3)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by striking assaults and inserting harassment and sexual assault cases ;\n**(B)**\nin paragraph (4), by inserting , including a synopsis of each sexual harassment and equal employment case and the disciplinary action taken, if any, with respect to each such case before the period at the end; and\n**(C)**\nby adding at the end the following:\n(5) A summary of the number of change of station, unit transfer, and change of work location requests submitted to the Secretary of Commerce, acting through the Under Secretary for Oceans and Atmosphere, under subsection (a) of section 3544, including the number of such requests the Secretary denied under that subsection. (6) A summary of the number of cases reported to the Commandant of the Coast Guard under section 3550. (7) The number of alleged sexual harassment and sexual assault cases involving fisheries observers, protected species observers, and endangered species observers, including\u2014 (A) a synopsis of each case and the status of each such case; (B) the disposition of any investigation; and (C) a description of the fishery management region and fishery or the geographic region and type of permitted operation in which the incident of sexual harassment or sexual assault is alleged to have occurred, as appropriate. ; and\n**(4)**\nin subsection (c), by striking assault and inserting harassment or sexual assault case .\n#### 5. Investigation and criminal referral requirements\n##### (a) Technical amendment\nSections 3548 and 3549 (33 U.S.C. 894e and 894f) are redesignated as sections 3551 and 3552, respectively.\n##### (b) Criminal referral\nSection 3547 ( 33 U.S.C. 894d\u20132 ) is amended\u2014\n**(1)**\nby striking pursuant to and inserting at the onset or during the course of ; and\n**(2)**\nby inserting and, with respect to a licensed mariner, the Commandant of the Coast Guard after United States Attorney .\n##### (c) In general\nSubtitle C of title XXXV ( 33 U.S.C. 894 et seq. ) is amended by inserting after section 3547 ( 33 U.S.C. 894d\u20132 ) the following:\n3548. Exceptions regarding anonymity of victims in certain cases (a) In general In any case in which an employee of the Administration, member of the commissioned officer corps of the Administration, or covered personnel elects restricted or unrestricted reporting under section 3541(b)(3)(B) or 3542(b)(5)(B), disclosure to the following persons or organizations of the personally identifying information of such individual is authorized for the following reasons: (1) To Administration staff or law enforcement personnel, if authorized by the victim in writing. (2) To Administration staff or law enforcement personnel to prevent or lessen a serious or imminent threat to the health or safety of the victim or another person. (3) To a victim advocate or healthcare provider, if required for the provision of victim services. (4) To a State or Federal court, if pursuant to a court order or if disclosure is required by Federal or State statute. (b) Notice of disclosure; privacy protection If information described in subsection (a) is disclosed under that subsection, the Secretary shall\u2014 (1) make reasonable attempts to provide notice to the individual the information of whom is so disclosed; and (2) take such action as is necessary to protect the privacy and safety of the individual. 3549. Restricted reporting update Not later than 3 years after the date of the enactment of the National Oceanic and Atmospheric Administration Sexual Harassment and Assault Prevention Improvements Act of 2025 , the Secretary of Commerce, acting through the Under Secretary for Oceans and Atmosphere, shall update the policies developed under sections 3541 and 3542 with respect to the mechanism established under subsections (b)(3)(B) and (b)(5)(B) of those sections, respectively, such that each such mechanism provides for a restricted reporting system that allows an employee of the Administration, member of the commissioned officer corps of the Administration, or covered personnel who alleges to have been sexually harassed or sexually assaulted to confidentially disclose the details of such sexual harassment or sexual assault to specified individuals and receive the services outlined in this subtitle\u2014 (1) without the dissemination of the personally identifying information of such individual, except as necessary for the provision of such services and as provided by section 3548(a); and (2) without automatically triggering an investigative process. 3550. Mariner reporting (a) Mandatory reporting by responsible entity of a vessel (1) Unrestricted reports The responsible entity of a vessel shall report to the Commandant of the Coast Guard any incident of sexual harassment or sexual assault in violation of employer policy or law, of which the responsible entity of a vessel is made aware, involving\u2014 (A) an employee or contractor of the Administration who is required to hold a valid merchant mariner credential as a condition of employment; or (B) a crewmember of a vessel that, at the time of such incident, was operating under a contract with the Administration. (2) Restricted reports Paragraph (1) does not apply with respect to an incident of sexual harassment or sexual assault reported on a restricted basis pursuant to the mechanisms established for such reporting under sections 3541(b)(3)(B) and 3542(b)(5)(B), respectively. (b) Reporting procedures (1) In general (A) Timing of reporting The responsible entity of a vessel shall make a report required under subsection (a)(1) as soon as the responsible entity of a vessel is made aware of the incident of sexual harassment or sexual assault that is the subject of the report. (B) Mode of reporting The responsible entity of a vessel shall make a report required under subsection (a)(1) to a single entity in the Coast Guard designated by the Commandant of the Coast Guard to receive such reports by the fastest telecommunication channel available to the responsible entity of a vessel. (2) Contents of report Each report made under this section shall include, to the best of the knowledge of the responsible entity of a vessel\u2014 (A) the name, Coast Guard merchant mariner credential reference number, if applicable, official position or role in relation to the vessel, and contact information of each individual involved in the incident of sexual harassment or sexual assault that is the subject of the report; (B) the name and official number of the vessel; (C) the time and date of the incident of sexual harassment or sexual assault; (D) the geographic position or location of the vessel when the incident of sexual harassment or sexual assault occurred; and (E) a brief description of the incident of alleged sexual harassment or sexual assault being reported. (c) Notification by Secretary (1) In general The Secretary of Commerce, acting through the Under Secretary for Oceans and Atmosphere, shall notify the Director of the Office of Marine and Aviation Operations of each report of an incident of sexual harassment or sexual assault received by the Secretary. (2) Notification contents Each notification under paragraph (1) shall include, to the best of the knowledge of the Secretary of Commerce, acting through the Under Secretary for Oceans and Atmosphere\u2014 (A) with respect to an unrestricted report submitted pursuant to section 3541(b)(3)(B) or 3542(b)(5)(B), the information required under subsection (b)(2) of this section; and (B) with respect to a restricted report submitted pursuant to section 3541(b)(3)(B) or 3542(b)(5)(B), the information required under subsection (b)(2) of this section that does not include the personally identifying information of the individual that submitted the restricted report. .\n#### 6. Definitions\nSection 3552, as redesignated by section 5(a) of this Act, is amended to read as follows:\n3552. Definitions In this subtitle: (1) Administration The term Administration means the National Oceanic and Atmospheric Administration. (2) Covered personnel (A) In general The term covered personnel means an individual who works with or conducts business on behalf of the Administration. (B) Inclusion The term covered personnel includes\u2014 (i) observers, at-sea monitors, and catch monitors required by the National Marine Fisheries Service to operate on or in commercial fishing vessels, other privately owned vessels, barges, or platforms, and shoreside processing facilities for\u2014 (I) commercial fisheries observation required by the Magnuson-Stevens Fishery Conservation and Management Act ( 13 U.S.C. 1801 et seq. ); (II) protected species or endangered species observation required by the Marine Mammal Protection Act of 1972 ( 16 U.S.C. 1361 et seq. ) or the Endangered Species Act of 1973 ( 16 U.S.C. 1351 et seq. ); or (III) platform removal observation; and (ii) voting members and executive and administrative staff of each Regional Fishery Management Council established by section 302 of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1852 ). (3) Responsible entity of a vessel The term responsible entity of a vessel means the Director of the Office of Marine and Aviation Operations, with respect to each vessel owned or operated by the Administration. (4) Sexual assault The term sexual assault has the meaning given the term in section 40002(a) of the Violence Against Women Act of 1994 (42 U.S.C. 13925 (a)). .\n#### 7. Conforming and clerical amendments\n##### (a) Conforming amendments\nSubtitle C of title XXXV ( 33 U.S.C. 894 et seq. ) is amended\u2014\n**(1)**\nby striking individuals who work with or conduct business on behalf of the Administration each place it appears and inserting covered personnel ; and\n**(2)**\nby striking National Oceanic and Atmospheric each place it appears, except\u2014\n**(A)**\nwhen it appears as National Oceanic and Atmospheric Administration Sexual Harassment and Assault Prevention Improvements Act of 2025 ;\n**(B)**\nin section 3551, in the section heading; and\n**(C)**\nin section 3552(1).\n##### (b) Clerical amendment\nEach of the tables of contents in section 2(b) and at the beginning of title XXXV are amended by striking the items relating to sections 3548 and 3549 and inserting the following:\nSec. 3548. Exceptions regarding anonymity of victims in certain cases. Sec. 3549. Restricted reporting update. Sec. 3550. Mariner referral. Sec. 3551. Annual report on sexual harassment, sexual assault, and equal employment in the National Oceanic and Atmospheric Administration. Sec. 3552. Definitions. .\n#### 8. Prohibited acts\nSection 307(1)(L) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1857(1)(L) ) is amended\u2014\n**(1)**\nby striking forcibly ; and\n**(2)**\nby striking on a vessel .\n#### 9. Prohibition on service in Commissioned Officer Corps of National Oceanic and Atmospheric Administration by individuals convicted of certain sexual offenses\nSection 261(a) of the National Oceanic and Atmospheric Administration Commissioned Officer Corps Act of 2002 ( 33 U.S.C. 3071(a) ) is amended\u2014\n**(1)**\nby redesignating paragraph (26) as paragraph (27); and\n**(2)**\nby inserting after paragraph (25) the following:\n(26) Section 657, relating to prohibition on service by individuals convicted of certain sexual offenses. .",
      "versionDate": "2025-03-27",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-21T21:12:27Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2406ih.xml"
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
      "title": "National Oceanic and Atmospheric Administration Sexual Harassment and Assault Prevention Improvements Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-08T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "National Oceanic and Atmospheric Administration Sexual Harassment and Assault Prevention Improvements Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Defense Authorization Act for Fiscal Year 2017 to address sexual harassment and sexual assault involving National Oceanic and Atmospheric Administration personnel, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T04:18:30Z"
    }
  ]
}
```
