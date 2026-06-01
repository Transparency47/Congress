# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5090?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5090
- Title: HONOR Act
- Congress: 119
- Bill type: HR
- Bill number: 5090
- Origin chamber: House
- Introduced date: 2025-09-02
- Update date: 2025-09-23T19:12:40Z
- Update date including text: 2025-09-23T19:12:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-02: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-09-02: Introduced in House

## Actions

- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-02",
    "latestAction": {
      "actionDate": "2025-09-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5090",
    "number": "5090",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "HONOR Act",
    "type": "HR",
    "updateDate": "2025-09-23T19:12:40Z",
    "updateDateIncludingText": "2025-09-23T19:12:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-02",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-02",
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
          "date": "2025-09-02T16:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5090ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5090\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 2, 2025 Ms. Mace introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo amend the Uniform Code of Military Justice to expand prohibitions against the wrongful broadcast, distribution, or publication of intimate visual images, including digital forgeries, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Halting Online Nonconsensual Offenses in the Ranks Act or the HONOR Act .\n#### 2. Modifications to offense of wrongful broadcast or distribution of intimate visual images under the uniform code of military justice\nSection 917a of title 10, united states code (article 117a of the uniform code of military justice) is amended to read as follows:\n917a. Art. 117a. Wrongful broadcast, distribution, or publication of intimate visual images (a) Prohibition Any person subject to this chapter\u2014 (1) who knowingly broadcasts, distributes, or uses a communication service to publish an authentic intimate visual depiction of an identifiable individual who is not a minor if\u2014 (A) the intimate visual depiction was obtained or created under circumstances in which the person knew or reasonably should have known the identifiable individual had a reasonable expectation of privacy; (B) the authentic intimate visual depiction was broadcast, distributed, or published without the consent of the identifiable individual; (C) what is depicted was not voluntarily exposed by the identifiable individual in a public or commercial setting; (D) what is depicted is not a matter of public concern; and (E) the broadcast, distribution, or publication of the intimate visual depiction\u2014 (i) is intended to cause harm; or (ii) causes harm, including psychological, financial, or reputational harm, to the identifiable individual; (2) who knowingly broadcasts, distributes, or uses a communication service to publish an authentic intimate visual depiction of an identifiable individual who is a minor with intent to\u2014 (A) abuse, humiliate, harass, or degrade the minor; or (B) arouse or gratify the sexual desire of any person; (3) who knowingly broadcasts, distributes, or uses a communication service to publish a digital forgery of an identifiable individual who is not a minor if\u2014 (A) the digital forgery was broadcast, distributed, or published without the consent of the identifiable individual; (B) what is depicted was not voluntarily exposed by the identifiable individual in a public or commercial setting; (C) what is depicted is not a matter of public concern; and (D) the broadcast, distribution, or publication of the digital forgery\u2014 (i) is intended to cause harm; or (ii) causes harm, including psychological, financial, or reputational harm, to the identifiable individual; or (4) who knowingly broadcasts, distributes, or uses a communication service to publish a digital forgery of an identifiable individual who is a minor with intent to\u2014 (A) abuse, humiliate, harass, or degrade the minor; or (B) arouse or gratify the sexual desire of any person, is guilty of wrongful distribution of intimate visual images or visual images of sexually explicit conduct and shall be punished as a court-martial may direct. (b) Exceptions Subsection (a) shall not apply to\u2014 (1) a lawfully authorized investigative, protective, or intelligence activity of\u2014 (A) a law enforcement agency of the United States, a State, or a political subdivision of a State; or (B) an intelligence agency of the United States; (2) a disclosure made reasonably and in good faith\u2014 (A) to a law enforcement officer or agency; (B) as part of a document production or filing associated with a legal proceeding; (C) as part of medical education, diagnosis, or treatment or for a legitimate medical, scientific, or educational purpose; (D) in the reporting of unlawful content or unsolicited or unwelcome conduct or in pursuance of a legal, professional, or other lawful obligation; or (E) to seek support or help with respect to the receipt of an unsolicited intimate visual depiction; (3) a disclosure reasonably intended to assist the identifiable individual; or (4) a person who possesses or publishes an intimate visual depiction of himself or herself engaged in nudity or sexually explicit conduct. (c) Consent For the purposes of subsection (a)\u2014 (1) the fact that the depicted individual consented to the creation of the intimate visual depiction shall not establish that the person consented to its disclosure; and (2) the fact that the depicted individual disclosed the intimate visual depiction to another person shall not establish that the depicted individual consented to the further disclosure of the intimate visual depiction. (d) Definitions In this section: (1) Consent The term consent means an affirmative, conscious, and voluntary authorization made by an individual free from force, fraud, duress, misrepresentation, or coercion. (2) Digital forgery The term digital forgery means any intimate visual depiction of an identifiable individual created through the use of software, machine learning, artificial intelligence, or any other computer-generated or technological means, including by adapting, modifying, manipulating, or altering an authentic visual depiction, that, when viewed as a whole by a reasonable person, is indistinguishable from an authentic visual depiction of the individual. (3) Identifiable individual The term identifiable individual means an individual\u2014 (A) who appears in whole or in part in an intimate visual depiction; and (B) whose face, likeness, or other distinguishing characteristic (including a unique birthmark or other recognizable feature) is displayed in connection with such intimate visual depiction. (4) Visual depiction The term visual depiction includes undeveloped film and videotape, data stored on computer disk or by electronic means which is capable of conversion into a visual image, and data which is capable of conversion into a visual image that has been transmitted by any means, whether or not stored in a permanent format. (5) Intimate visual depiction The term intimate visual depiction \u2014 (A) means a visual depiction that depicts\u2014 (i) the uncovered genitals, pubic area, anus, or female nipple of an identifiable individual; or (ii) the display or transfer of bodily sexual fluids\u2014 (I) on to any part of the body of an identifiable individual; (II) from the body of an identifiable individual; or (iii) an identifiable individual engaging in sexually explicit conduct; and (B) includes any visual depictions described in subparagraph (A) produced while the identifiable individual was in a public place only if the individual did not\u2014 (i) voluntarily display the content depicted; or (ii) consent to the sexual conduct depicted. (6) Sexually explicit conduct The term sexually explicit conduct means actual or simulated\u2014 (A) sexual intercourse, including genital-genital, oral-genital, anal-genital, or oral-anal, whether between persons of the same or opposite sex; (B) bestiality; (C) masturbation; (D) sadistic or masochistic abuse; or (E) lascivious exhibition of the genitals or pubic area of any person. (7) Minor The term minor means any individual under the age of 18 years. (8) Broadcast The term broadcast means to electronically transmit a visual image with the intent that it be viewed by a person or persons. (9) Distribute The term distribute means to deliver to the actual or constructive possession of another person, including transmission by mail or electronic means. (10) Communications service The term communications service means\u2014 (A) a service provided by a person that is a common carrier; (B) an electronic communication service; (C) an information service; or (D) an interactive computer service. (11) Common carrier The term common carrier means any person engaged as a common carrier for hire, in interstate or foreign communication by wire or radio or interstate or foreign radio transmission of energy, but a person engaged in radio broadcasting shall not, insofar as such person is so engaged, be deemed a common carrier. (12) Electronic communication service The term electronic communication service means any service which provides to users thereof the ability to send or receive wire or electronic communications. (13) Information service The term information service means the offering of a capability for generating, acquiring, storing, transforming, processing, retrieving, utilizing, or making available information via telecommunications, and includes electronic publishing, but does not include any use of any such capability for the management, control, or operation of a telecommunications system or the management of a telecommunications service. (14) Interactive computer service The term interactive computer service means any information service, system, or access software provider that provides or enables computer access by multiple users to a computer server, including specifically a service or system that provides access to the Internet and such systems operated or services offered by libraries or educational institutions. .",
      "versionDate": "2025-09-02",
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
        "actionDate": "2025-09-10",
        "actionTime": "17:56:43",
        "text": "The Clerk was authorized to correct section numbers, punctuation, and cross references, and to make other necessary technical and conforming corrections in the engrossment of H.R. 3838."
      },
      "number": "3838",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Streamlining Procurement for Effective Execution and Delivery and National Defense Authorization Act for Fiscal Year 2026",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-23T18:23:37Z"
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
      "date": "2025-09-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5090ih.xml"
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
      "title": "HONOR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-10T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HONOR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-10T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Halting Online Nonconsensual Offenses in the Ranks Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-10T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Uniform Code of Military Justice to expand prohibitions against the wrongful broadcast, distribution, or publication of intimate visual images, including digital forgeries, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-10T04:18:25Z"
    }
  ]
}
```
