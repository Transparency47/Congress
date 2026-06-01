# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8470?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8470
- Title: Surveillance Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 8470
- Origin chamber: House
- Introduced date: 2026-04-23
- Update date: 2026-04-30T20:32:52Z
- Update date including text: 2026-04-30T20:32:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-23: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-23: Introduced in House

## Actions

- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-23",
    "latestAction": {
      "actionDate": "2026-04-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8470",
    "number": "8470",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001184",
        "district": "4",
        "firstName": "Thomas",
        "fullName": "Rep. Massie, Thomas [R-KY-4]",
        "lastName": "Massie",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Surveillance Accountability Act",
    "type": "HR",
    "updateDate": "2026-04-30T20:32:52Z",
    "updateDateIncludingText": "2026-04-30T20:32:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-23",
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
      "actionDate": "2026-04-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-23",
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
          "date": "2026-04-23T13:01:40Z",
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
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8470ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8470\nIN THE HOUSE OF REPRESENTATIVES\nApril 23, 2026 Mr. Massie (for himself and Ms. Boebert ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to ensure that all searches that significantly impinge on the privacy or security of a person require a warrant based on probable cause, to provide a right of action for violations of Fourth Amendment rights, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Surveillance Accountability Act .\n#### 2. Warrant requirement for searches\n##### (a) In general\nChapter 205 of title 18, United States Code, is amended by adding at the end the following new section:\n3119. Searches to accord with the Fourth Amendment (a) Warrant requirement (1) In general Except as provided in subsection (b), no search may be conducted without a warrant issued by a neutral and detached magistrate upon probable cause, supported by oath or affirmation, and particularly describing the place to be searched and the persons or things to be seized. (2) Third-Party Data (A) Presumption of privacy The government shall not access any data, metadata, or personal information held by a third party, including financial services providers, telecommunication service providers, internet service providers, cloud storage companies, or data brokers, without a valid warrant, regardless of whether the third party consents or cooperates. (B) Exception invalidated No contractual agreement between a user and a third party may be interpreted as waiving the government\u2019s warrant requirement for access to the data of that user, unless such waiver is knowing, voluntary, and explicit. (b) Exceptions The following may be conducted without a warrant: (1) Plain-view searches. (2) The verification of government-issued primary photo identification documents during a stop of a motor vehicle, travel, or other interactions with law enforcement, including the verification of\u2014 (A) a State identification card; (B) a driver\u2019s license; (C) a passport; (D) a passport card; (E) a military identification; or (F) a permanent resident card. (3) The collection or analysis of information that is lawfully published or voluntarily made available by a person or entity to a public audience, and which requires no circumvention of privacy settings, encryption, or other access controls. (4) The use of lawful investigative techniques to collect data from publicly available sources such as new outlets, official government publications, public records, or user-posted content that is clearly accessible to the general public without special access or tools. (5) Searches conducted with consent. (6) Searched conducted under exigent circumstances. (c) Limitations The exceptions described in subsection (b) shall not be construed to permit the warrantless collection, retention, querying, or analysis of data exposed to public view or accessible to a third party if the person associated with the collected identifiers did not express informed and voluntary consent to such collection with respect to data gathered by entering a public place, operating a motor vehicle on a public roadway, or patronizing a private establishment open to the public, including\u2014 (1) biometric data, including facial images, faceprints, gait, voice recognition, or other unique physical identifiers, obtained through facial recognition systems or comparable surveillance technologies; or (2) license plate images, vehicle metadata, or vehicle movement patterns obtained through automated license plate readers or similar systems. (d) Definitons In this section: (1) Search The term search means any government-initiated act that intrudes upon an individual\u2019s reasonable expectation of privacy, including the following: (A) Investigatory acts Any investigatory act purposefully directed at a specific person or entity, or the property of a specific person or entity, with the intent of obtaining information not otherwise available to the public. (B) Government surveillance and monitoring Any non-consensual surveillance, monitoring, or inquiry conducted by a government entity or its agents, whether through human, digital, or automated means, that collects information on a specific individual or entity, including information on that individual or entity\u2019s\u2014 (i) communications; (ii) associations; (iii) employment; (iv) social media usage; (v) internet usage; (vi) financial transactions; or (vii) travel. (C) Collection of personal data The acquisition and analysis of any data, metadata, or information pertaining to a person\u2019s digital or physical life, including\u2014 (i) geolocation; (ii) communication records; (iii) personal device activity; (iv) assets; (v) liabilities; (vi) biometric identifiers; (vii) behavioral signals data; or (viii) financial transactions. (2) Plain-view searches defined In this section, the term plain-view searches means the observation or seizure of evidence by a law enforcement officer who is lawfully present at a location, where the incriminating nature of the evidence is immediately apparent, and where such observation is incidental to the officer\u2019s lawful presence and does not involve the use of enhanced surveillance technology or systematic monitoring. (e) Rule of construction Nothing in this section shall be construed to\u2014 (1) modify, supersede, or limit any existing constitutional protection, or to authorize surveillance that would otherwise be unlawful; (2) eliminate or restrict constitutionally recognized exceptions permitting brief investigatory detentions or protective frisks based on reasonable suspicion; or (3) eliminate or restrict the authority of law enforcement officers to conduct brief investigatory detentions, protective frisks, arrests, or searches incident to ordinary criminal law enforcement encounters. .\n##### (b) Clerical amendment\nThe table of sections for chapter 205 of title 18, United States Code, amended by adding at the end the following:\n3119. Searches to accord with the Fourth Amendment. .\n#### 3. Right of action for violations of Fourth Amendment rights\n##### (a) In general\nThe Revised Statutes are amended by inserting after section 1979 the following:\n1979A. Deprivation of Fourth Amendment rights (a) In general Every person, including a Federal employee, who, under color of any statute, ordinance, regulation, custom, or usage, of the United States, subjects, or causes to be subjected, any citizen of the United States or any person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Fourth Amendment, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress. (b) Attorney\u2019s fees In any action, suit, or proceeding to enforce this Act, the court, in its discretion, may allow the prevailing party, other than the United States, a reasonable attorney\u2019s fee as part of the costs. (c) Federal employee defined In this section, the term Federal employee means an individual other than the President or the Vice President, who occupies a position in any agency or instrumentality of the executive branch (including any independent agency). (d) Rule of construction Nothing in this section shall be construed to authorize a Federal employee to bring a suit against their Federal employer or the Federal Government for conduct that is within the scope of the employment relationship. .\n##### (b) Severability\nIf any provision of this Act or the application of such provision to any person or circumstance is held to be unconstitutional, the remainder of this Act, and the application of this Act, to any other person or circumstance, shall not be affected thereby.",
      "versionDate": "2026-04-23",
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
        "updateDate": "2026-04-30T20:32:52Z"
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
      "date": "2026-04-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8470ih.xml"
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
      "title": "Surveillance Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-24T08:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Surveillance Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-24T08:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to ensure that all searches that significantly impinge on the privacy or security of a person require a warrant based on probable cause, to provide a right of action for violations of Fourth Amendment rights, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-24T08:18:44Z"
    }
  ]
}
```
