# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7785?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7785
- Title: Protecting Our Communities Act
- Congress: 119
- Bill type: HR
- Bill number: 7785
- Origin chamber: House
- Introduced date: 2026-03-04
- Update date: 2026-05-16T08:07:02Z
- Update date including text: 2026-05-16T08:07:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-04 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-05 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- Latest action: 2026-03-04: Introduced in House

## Actions

- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-04 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-05 - Committee: Referred to the Subcommittee on Border Security and Enforcement.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7785",
    "number": "7785",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "B001281",
        "district": "3",
        "firstName": "Joyce",
        "fullName": "Rep. Beatty, Joyce [D-OH-3]",
        "lastName": "Beatty",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "Protecting Our Communities Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:02Z",
    "updateDateIncludingText": "2026-05-16T08:07:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-05",
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
      "actionCode": "H11100",
      "actionDate": "2026-03-04",
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
      "actionDate": "2026-03-04",
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
      "actionDate": "2026-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-04",
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
          "date": "2026-03-04T15:04:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-05T05:00:00Z",
              "name": "Referred to"
            }
          },
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-04T15:04:10Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7785ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7785\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2026 Mrs. Beatty introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Homeland Security , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo improve accountability and training for Immigration and Customs Enforcement.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Protecting Our Communities Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec.\u20021.\u2002Short title; table of contents.\nSec.\u20022.\u2002Body cameras.\nSec.\u20023.\u2002Insignia and identification required for law enforcement officers and agents engaged in border security or immigration enforcement.\nSec.\u20024.\u2002Deescalation traning.\nSec.\u20025.\u2002Requiring notification for local law enforcement.\nSec.\u20026.\u2002Reporting Requirements.\n#### 2. Body cameras\n##### (a) Body and vehicle camera requirements\n**(1) In general**\nNot later than 90 days after the date of enactment of this section, the Secretary of Homeland Security shall develop and disseminate a Department-wide directive requiring the use of\u2014\n**(A)**\nbody-worn cameras by all Federal immigration enforcement personnel; and\n**(B)**\ndashboard cameras for all vehicles being used in Federal immigration enforcement operations and associated recording protocols.\n**(2) Requirement for body camera**\nA body camera required under paragraph (1) shall\u2014\n**(A)**\nhave a field of view at least as broad as the officer\u2019s vision; and\n**(B)**\nbe worn in a manner that maximizes the camera\u2019s ability to capture video footage of the officer\u2019s activities.\n**(3) Requirement to activate**\n**(A) In general**\nBoth the video and audio recording functions of the body camera shall be activated whenever a Federal immigration enforcement personnel is participating in a Federal immigration enforcement operation, except that when an immediate threat to the person\u2019s life or safety makes activating the camera impossible or dangerous the Federal immigration enforcement personnel shall activate the camera at the first reasonable opportunity to do so.\n**(B) Allowable deactivation**\nThe body camera shall not be deactivated until the Federal immigration enforcement operation ceases and the Federal immigration enforcement personnel leaves the scene.\n**(4) Limitations on use of body camera**\nBody cameras shall not be used to gather intelligence information based on First Amendment protected speech, associations, or religion, or to record activity that is unrelated to a Federal immigration enforcement operation, and shall not be equipped with or employ any facial recognition technologies.\n**(5) Retention of footage**\n**(A) In general**\nBody camera and dashboard camera video footage shall be retained by the Department of Homeland Security for one year after the date on which it was recorded, after which time such footage shall be permanently deleted.\n**(B) Right to inspect**\nDuring the one year retention period described in paragraph (1), the following persons shall have the right to inspect the body camera footage:\n**(i)**\nAny person who is a subject of body camera video footage, and their designated legal counsel.\n**(ii)**\nA parent or legal guardian of a minor subject of body camera video footage, and their designated legal counsel.\n**(iii)**\nThe spouse, next of kin, or legally authorized designee of a deceased subject of body camera video footage, and their designated legal counsel.\n**(iv)**\nA Federal immigration enforcement personnel whose body camera recorded the video footage, and their designated legal counsel, subject to the limitations and restrictions in this Act.\n**(v)**\nThe superior officer of a Federal immigration enforcement personnel whose body camera recorded the video footage, subject to the limitations and restrictions in this Act.\n**(vi)**\nAny defense counsel who claims, pursuant to a written affidavit, to have a reasonable basis for believing a video may contain evidence that exculpates a client.\n**(6) Principles**\nIn preparing the directive required under paragraph (1), the Secretary of Homeland Security shall include the following:\n**(A)**\nBenchmarks for implementation of the use of body-worn cameras by Federal immigration enforcement personnel and dashboard cameras for vehicles being used for Federal immigration enforcement to conform with a standard that cameras are on by default and may only be turned off in certain circumstances.\n**(B)**\nTraining requirements, procedures, and best practices for the use of body-worn cameras and dashboard cameras.\n**(C)**\nPlans to publicize the directive and the requirements set forth in this section to ensure Federal immigration enforcement personnel and other impacted individuals are notified of new policies.\n#### 3. Insignia and identification required for law enforcement officers and agents engaged in border security or immigration enforcement\n##### (a) In general\nTitle VII of the Homeland Security Act of 2002 ( 6 U.S.C. 341 et seq. ) is amended by adding at the end the following new section:\n714. Insignia and identification required for law enforcement officers and agents engaged in border security or immigration enforcement (a) Requirements (1) In general If a law enforcement officer or agent of the Department detains or arrests an individual in connection with a border security or immigration enforcement function of such officer or agent, during such detention or arrest, as the case may be, such officer or agent\u2014 (A) shall\u2014 (i) provide such individual with an identification of the component of the Department that employs such officer or agent; and (ii) display or wear the official insignia or uniform of such officer or agent in a manner that is visible to individuals other than such officer or agent; and (B) may not wear a face covering or any other item that conceals the face of such officer or agent. (2) Rule of construction Nothing in this subsection may be construed to limit or prohibit the use of tactical gear by law enforcement officers and agents consistent with the policies and procedures of the Department. (3) Reports (A) Initial report Not later than 30 days after the date of enactment of this section, the Secretary shall submit to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a report on the policies and procedures of the Department regarding the use of tactical gear by law enforcement officers and agents of the Department. (B) Updates If the Secretary modifies the policies or procedures of the Department regarding the use of tactical gear by law enforcement officers or agents of the Department, not later than 30 days after any such modification, the Secretary shall submit to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a report relating thereto. (b) Research and development The Secretary, acting through the Under Secretary for Science and Technology, and in coordination with the heads of components of the Department that employ law enforcement officers or agents, shall carry out research and development of technology to maximize the visibility of the official insignia or uniform of such an officer or agent to be utilized during detentions or arrests, including technology to maximize such visibility in response to certain factors in connection with such detentions or arrests, including the following: (1) Location. (2) Time of day. (3) Weather. (c) Definitions In this section: (1) Law enforcement officer or agent The term law enforcement officer or agent means a law enforcement officer or agent of the Department, including U.S. Immigration and Customs Enforcement and U.S. Customs and Border Protection. (2) Official insignia or uniform The term official insignia or uniform has the meaning given such term in section 716 of title 18, United States Code. .\n##### (b) Clerical amendment\nThe table of contents for such Act is amended by inserting after the item pertaining to section 713 the following:\n714. Insignia and identification required for law enforcement officers and agents engaged in border security or immigration enforcement. .\n#### 4. Deescalation traning\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Secretary of Homeland Security shall develop training curricula or identify effective existing training curricula for Federal immigration enforcement personnel regarding\u2014\n**(1)**\ndeescalation tactics; and\n**(2)**\nalternatives to use of force.\n##### (b) Particular inclusions\nThe training curricula developed or identified under subsection (a) shall include\u2014\n**(1)**\nscenario-based exercises;\n**(2)**\npretraining and posttraining tests to assess relevant knowledge and skills covered in the training curricula; and\n**(3)**\nfollowup evaluative assessments to determine the degree to which participants in the training apply, in their jobs, the knowledge and skills gained in the training.\n##### (c) Consultation required\nThe Secretary of Homeland Security shall develop and identify training curricula under this section in consultation with relevant law enforcement agencies of States and units of local government, immigrant organizations, associations that represent individuals with mental or behavioral health diagnoses or individuals with disabilities, labor organizations, professional law enforcement organizations, local law enforcement labor and representative organizations, law enforcement trade associations, mental health and suicide prevention organizations, family advocacy organizations, and civil rights and civil liberties groups.\n#### 5. Requiring notification for local law enforcement\nFederal immigration enforcement shall notify local law enforcement of impending operations in their jurisdiction.\n#### 6. Reporting Requirements\nBeginning not later than 3 months after the date of enactment of this section, the Secretary of Homeland Security shall submit to Congress the following reports on the criteria Federal immigration enforcement personnel use to determine whether an immigrant poses a public safety or national security threat:\n**(1)**\nThe Secretary of Homeland Security shall submit to Congress a report every 6 months detailing\u2014\n**(A)**\ninstances where nondeadly force was used;\n**(B)**\nthe level of public safety or national security threat the target posed;\n**(C)**\nfor what reason nondeadly force was administered;\n**(D)**\nspecific instances where nondeadly force was improperly administered; and\n**(E)**\nthe measures the Department took to ensure accountability for improper use of force.\n**(2)**\nThe Secretary of Homeland Security shall submit to Congress a report every 6 months detailing instances of assaults against Federal immigration enforcement personnel. The report shall include\u2014\n**(A)**\nthe total number of personnel involved in immigration enforcement operations;\n**(B)**\nthe number of assaults against Federal immigration enforcement personnel; and\n**(C)**\ndetails on the severity of those instances.\n**(3)**\nThe Secretary of Homeland Security shall send a report to Congress every 6 months detailing all instances in which Federal immigration enforcement personnel operated without displaying or wearing the official insignia or uniform.",
      "versionDate": "2026-03-04",
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
        "actionDate": "2025-06-27",
        "text": "Referred to the Subcommittee on Border Security and Enforcement."
      },
      "number": "4176",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "No Secret Police Act of 2025",
      "type": "HR"
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
        "updateDate": "2026-03-09T17:17:28Z"
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
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7785ih.xml"
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
      "title": "Protecting Our Communities Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T09:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Our Communities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-05T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve accountability and training for Immigration and Customs Enforcement.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-05T09:18:21Z"
    }
  ]
}
```
