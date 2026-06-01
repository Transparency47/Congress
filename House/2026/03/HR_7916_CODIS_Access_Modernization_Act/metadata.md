# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7916?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7916
- Title: CODIS Access Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 7916
- Origin chamber: House
- Introduced date: 2026-03-12
- Update date: 2026-04-01T18:11:02Z
- Update date including text: 2026-04-01T18:11:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-03-12: Introduced in House

## Actions

- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7916",
    "number": "7916",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "N000026",
        "district": "22",
        "firstName": "Troy",
        "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
        "lastName": "Nehls",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "CODIS Access Modernization Act",
    "type": "HR",
    "updateDate": "2026-04-01T18:11:02Z",
    "updateDateIncludingText": "2026-04-01T18:11:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
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
      "actionDate": "2026-03-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T13:33:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7916ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7916\nIN THE HOUSE OF REPRESENTATIVES\nMarch 12, 2026 Mr. Nehls introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 34, United States Code, to authorize eligible privately owned and operated forensic DNA testing laboratories to directly upload qualifying DNA profiles to the National DNA Index System, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the CODIS Access Modernization Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nCongress recognizes the essential role that publicly operated forensic laboratories and their dedicated scientific professionals play in supporting law enforcement investigations, administering justice, and protecting public safety. However, increasing case volumes, persistent DNA testing backlogs, and the challenges associated with implementing emerging forensic technologies within government systems can delay the timely processing of critical evidence. These delays may hinder the identification and apprehension of violent offenders, allowing serial perpetrators of crimes such as rape and homicide to remain unidentified and potentially continue victimizing additional individuals. Congress further finds that strategic public-private partnerships with accredited forensic laboratories can expand testing capacity, accelerate the processing of DNA evidence, and provide access to advanced technologies and specialized expertise. Such partnerships can also reduce delays in DNA profile entry into the National DNA Index System, accelerate investigative leads, increase case resolution rates, reduce burdens on publicly operated laboratories, enhance justice for victims and their families, and help prevent future crimes.\n**(2)**\nAccredited private forensic DNA laboratories, meeting the same FBI Quality Assurance Standards and ISO/IEC 17025 requirements as public laboratories, are currently barred from direct uploads to the Combined DNA Index System (CODIS), resulting in mandatory and costly redundant reviews that delay investigations by days to years.\n**(3)**\nRestricting CODIS access to public laboratories is detrimental to national security and public safety, as violent offenders often cross jurisdictions, while private labs already process thousands of cases annually for Federal, State, local, military, and homeland security agencies.\n**(4)**\nPrecedent exists for non-law enforcement entities to officially perform traditional criminal justice agency functions, including the Department of Justice\u2019s partnership with the National Center for Missing and Exploited Children (NCMEC) which affords it vital access to the National Crime Information Center (NCIC) to help solve missing and unidentified children\u2019s cases across the United States.\n**(5)**\nThe United States Government routinely relies on accredited private entities and government contractors to perform highly sensitive national security, intelligence, and law enforcement support functions, including cybersecurity operations, forensic analysis, intelligence processing, and classified systems management under strict Federal oversight and security requirements. The use of qualified private forensic laboratories to support DNA identification efforts represents a continuation of established Federal practices of leveraging private sector expertise to advance public safety.\n**(6)**\nAccredited private forensic DNA laboratories already perform forensic testing for Federal, State, local, military, and homeland security agencies while complying with the same FBI Quality Assurance Standards and ISO/IEC 17025 accreditation requirements as public laboratories.\n**(7)**\nAllowing qualified private forensic DNA laboratories to upload qualifying DNA profiles to the National DNA Index System under strict regulatory safeguards is consistent with longstanding Federal practices of utilizing accredited private entities to enhance national security, public safety, and investigative capabilities.\n**(8)**\nThe societal and economic costs of unsolved violent crimes are immense, with estimates of $122,000 per rape and $1.4 million per murder in medical, productivity, legal, and suffering-related expenses. Timely offender identification and apprehension also prevent future crimes as rapists commit on average more than 7 sexual assaults per year.\n**(9)**\nGranting direct CODIS upload authority to eligible private laboratories would accelerate case resolutions, increase DNA matches and arrests, reduce public lab burdens, prevent additional offenses, and advance bipartisan priorities of public safety, victim rights, and efficient private sector utilization.\n#### 3. Direct access for eligible private forensic dna laboratories to the national dna index system\n##### (a) In general\nThe Attorney General shall allow eligible privately owned and operated forensic evidence DNA testing laboratories to directly upload qualifying DNA profiles to the National DNA Index System (NDIS).\n##### (b) Regulations\nThe Department of Justice and the Federal Bureau of Investigation shall issue regulations to implement and carry out this section, including criteria for eligibility, procedures for direct upload, security and privacy safeguards, and any other requirements necessary to ensure compliance with Federal law, not later than six months after the date of enactment.\n##### (c) Limitation of authority\nNothing in this Act shall be construed to grant privately owned and operated forensic DNA laboratories access to search, query, or retrieve information from the National DNA Index System beyond the authorized submission of qualifying DNA profiles in accordance with Federal Bureau of Investigation regulations and applicable law.\n##### (d) Definitions\nIn this section:\n**(1)**\nThe term privately owned and operated forensic evidence DNA testing laboratory means a private DNA forensic evidence testing laboratory that\u2014\n**(A)**\nhas been accredited for a minimum of five consecutive years to the ISO/IEC 17025 standards by a nationally recognized nonprofit professional association of persons actively involved in forensic science;\n**(B)**\nundergoes external audits every two years that demonstrate compliance with the Quality Assurance Standards established by the Director of the Federal Bureau of Investigation;\n**(C)**\ndemonstrates compliance with the limited access requirements for DNA samples and records in accordance with Federal law;\n**(D)**\ndemonstrates compliance with the provisions of the NDIS Memorandum of Understanding and the NDIS Operational Procedures Manual; and\n**(E)**\nis not owned or managed by a governmental organization.\n**(2)**\nThe term qualifying DNA profiles means DNA profiles that meet the standards and eligibility requirements for entry into the National DNA Index System, as determined by the Federal Bureau of Investigation.\n**(3)**\nThe term National DNA Index System or NDIS means the index established under section 12592 of title 34, United States Code.\n#### 4. Conforming amendments\nThe Attorney General, in consultation with the Director of the Federal Bureau of Investigation, shall make such conforming amendments to regulations, policies, and procedures (including updates to the NDIS Memorandum of Understanding and the NDIS Operational Procedures Manual) as may be necessary to carry out this Act.\n#### 5. Effective date\nThis Act shall take effect on the date of its enactment, except that the requirement to issue regulations under section 3(b) shall apply as specified in that subsection.",
      "versionDate": "2026-03-12",
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
        "updateDate": "2026-04-01T18:11:02Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7916ih.xml"
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
      "title": "CODIS Access Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-28T12:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CODIS Access Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-28T12:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 34, United States Code, to authorize eligible privately owned and operated forensic DNA testing laboratories to directly upload qualifying DNA profiles to the National DNA Index System, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-28T12:18:25Z"
    }
  ]
}
```
