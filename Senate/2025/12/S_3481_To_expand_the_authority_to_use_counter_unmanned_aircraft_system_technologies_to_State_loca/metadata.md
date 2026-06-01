# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3481?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3481
- Title: SAFER SKIES Act
- Congress: 119
- Bill type: S
- Bill number: 3481
- Origin chamber: Senate
- Introduced date: 2025-12-15
- Update date: 2026-04-02T16:34:00Z
- Update date including text: 2026-04-02T16:34:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-15: Introduced in Senate
- 2025-12-15 - IntroReferral: Introduced in Senate
- 2025-12-15 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-12-15: Introduced in Senate

## Actions

- 2025-12-15 - IntroReferral: Introduced in Senate
- 2025-12-15 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-15",
    "latestAction": {
      "actionDate": "2025-12-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3481",
    "number": "3481",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "P000595",
        "district": "",
        "firstName": "Gary",
        "fullName": "Sen. Peters, Gary C. [D-MI]",
        "lastName": "Peters",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "SAFER SKIES Act",
    "type": "S",
    "updateDate": "2026-04-02T16:34:00Z",
    "updateDateIncludingText": "2026-04-02T16:34:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-15",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-12-16T00:02:07Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "IA"
    },
    {
      "bioguideId": "J000293",
      "firstName": "Ron",
      "fullName": "Sen. Johnson, Ron [R-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "WI"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3481is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3481\nIN THE SENATE OF THE UNITED STATES\nDecember 15, 2025 Mr. Peters (for himself, Mr. Grassley , Mr. Johnson , and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo expand the authority to use counter-unmanned aircraft system technologies to State, local, Tribal, and territorial law enforcement and correctional agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the SAFER SKIES Act .\n#### 2. Drone countermeasures to protect public safety and critical infrastructure\nSection 210G of the Homeland Security Act of 2002 ( 6 U.S.C. 124n ) is amended\u2014\n**(1)**\nby striking subsection (a) and inserting the following:\n(a) Authorities (1) Authority of the Department of Homeland Security and Department of Justice Notwithstanding section 46502 of title 49, United States Code, or sections 32, 1030, 1367 and chapters 119 and 206 of title 18, United States Code, the Secretary and the Attorney General may, for their respective Departments, take and may authorize personnel to take such actions as are described in subsection (b)(1) that are necessary to enforce the law, protect the public, or to mitigate a credible threat that an unmanned aircraft system or unmanned aircraft poses to the safety or security of a covered facility or asset. (2) Authority of State, local, Tribal, and territorial law enforcement and correctional agencies Notwithstanding section 46502 of title 49, United States Code, or sections 32, 1030, 1367 and chapters 119 and 206 of title 18, United States Code, notwithstanding the laws of any particular State, local, Tribal, or territorial jurisdiction, and after completing the training detailed in subsection (d)(2), any State, local, Tribal, or territorial law enforcement or correctional agency may, subject to subsection (d)(2), take, and authorize personnel with assigned duties that include the security or protection of people, facilities, or assets, to take such actions as are described in subsection (b)(1) that are necessary to mitigate a credible threat that an unmanned aircraft system or unmanned aircraft poses to the safety or security of people, facilities, and assets, a venue or set of venues used for large-scale public gatherings or events, critical infrastructure, or correctional facilities. ;\n**(2)**\nin subsection (b)(1)(B), by striking and electromagnetic means and inserting electromagnetic means, and through the use of remote identification broadcast or other means ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nby inserting pursuant to subsection (a)(1) after Attorney General ;\n**(B)**\nby striking Any unmanned and inserting the following:\n(1) Federal agencies Any unmanned ; and\n**(C)**\nby adding at the end the following:\n(2) Other agencies Any unmanned aircraft system or unmanned aircraft described in subsection (a) that is seized by a State, local, Tribal, or territorial law enforcement or correctional agency pursuant to subsection (a)(2) is subject to forfeiture under the laws of the agency's jurisdiction. ;\n**(4)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (1), by striking or the Attorney General and inserting , the Attorney General, or any State, local, Tribal, or territorial law enforcement or correctional agency ;\n**(B)**\nby redesignating paragraph (2) as paragraph (3); and\n**(C)**\nby inserting after paragraph (1) the following:\n(2) State, local, Tribal, and territorial law enforcement training and certification (A) Training and certification required (i) In general Only State, local, Tribal, or territorial law enforcement and correctional officers who have been trained and certified by the Attorney General, or the Attorney General\u2019s designee, in coordination with the Secretary of Homeland Security through a national schoolhouse which will serve as the sole certifying authority for State, local, Tribal, territorial, and correctional officers in the use of the authority granted under subsection (a)(2), may exercise authorities in subsection (b)(1)(C), (D), and (F). (ii) Training and certification procedures The Attorney General, in coordination with the Secretary of Homeland Security, the Secretary of Defense, and the Secretary of Transportation, shall, not later than 180 days after the date of enactment of the SAFER SKIES Act , develop training and certification procedures for the use of the authority described in subsection (a)(2) that State, local, Tribal, and territorial law enforcement and correctional officers shall be required to satisfy before taking any actions described in subsection (b)(1). (iii) Technologies Technologies used by State, local, Tribal, and territorial law enforcement or correctional agencies to take actions described in subsection (b)(1) shall be limited to systems or technologies that are included on a list of authorized technologies maintained jointly by the Department of Justice, the Department of Homeland Security, the Department of Defense, the Department of Transportation, the Federal Communications Commission, and the National Telecommunications and Information Administration. (B) Oversight The Attorney General, in coordination with the Secretary of Homeland Security and the Administrator of the Federal Aviation Administration, shall oversee compliance with the requirements set forth in subsection (e) with respect to the use of the authority granted under subsection (a)(2) by each State, local, Tribal, and territorial law enforcement agency that has been certified pursuant to the training and certification requirements described in subparagraph (A). (C) State, local, tribal, and territorial law enforcement and correctional agencies mitigation notification requirement (i) In general Any State, local, Tribal, or territorial law enforcement or correctional agency exercising authority under subsection (a)(2) shall, within 48 hours of taking any mitigation action described in subsection (b)(1), submit a notification to the Attorney General and the Secretary of Homeland Security containing\u2014 (I) the date, time, and geographic location of the mitigation action; (II) a brief description of the credible threat or safety concern necessitating such action; (III) the type of mitigation capability employed; and (IV) any known operational effects, including the seizure, disabling, or destruction of an unmanned aircraft system or unmanned aircraft. (ii) Report mechanism The Attorney General and the Secretary of Homeland Security shall establish a streamlined and secure submission mechanism to support the notification requirement under clause (i). (D) Reports Not later than 1 year after the date of enactment of the SAFER SKIES Act , and biannually thereafter, the Attorney General, in coordination with the Secretary of Homeland Security and the Secretary of Transportation, shall submit to the appropriate congressional committees an unclassified report with a classified annex on activities carried out by State, local, Tribal, and territorial law and correctional enforcement agencies exercising the authority granted under subsection (a)(2) and subject to the training and certification requirements described in subparagraph (A), including\u2014 (i) a description of the training and certification procedures developed and implemented pursuant to subparagraph (A)(ii); (ii) a list of State, local, Tribal, and territorial law enforcement and correctional agencies that applied for and were certified to exercise the authorities granted by subsection (a)(2); (iii) a list of currently authorized technologies pursuant to subparagraph (A)(iii); (iv) the frequency, location, and circumstances of State, local, Tribal, territorial, and correctional officers mitigation deployments and types of mitigation employed; (v) a list of any aviation security or safety incidents that occurred due to State, local, Tribal, territorial, and correctional officers deployment of counter-UAS technologies; (vi) recommendations for improving State, local, Tribal, and territorial law and correctional agencies counter-UAS training, oversight, compliance, and execution and the compliance audits required by section 6(b)(2) of the SAFER SKIES Act ; and (vii) a determination on if State, local, Tribal, and territorial law and correctional agencies are able to fully protect critical infrastructure from the drone threat and if not, recommendations on how to expand counter-UAS authorities to critical infrastructure owners. ;\n**(5)**\nin subsection (e)\u2014\n**(A)**\nin the matter preceding paragraph (1), by striking or the Attorney General and inserting , the Attorney General, or any State, local, Tribal, or territorial law enforcement or correctional agency ;\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nby striking or the Attorney General and inserting , the Attorney General, or any State, local, Tribal, or territorial law enforcement or correctional agency ;\n**(ii)**\nby inserting , State, local, Tribal, or territorial after Federal ; and\n**(iii)**\nby inserting (as applicable) after law ;\n**(C)**\nin paragraph (4), in the matter preceding subparagraph (A), by striking or the Department of Justice and inserting the Department of Justice, or the State, local, Tribal, or territorial law enforcement or correctional agency ; and\n**(D)**\nin paragraph (5)\u2014\n**(i)**\nby striking tribal and inserting Tribal ; and\n**(ii)**\nby inserting other than those of an aeronautical communications system, as allowed for in section 2511(2)(g)(ii)(IV) of title 18, United States Code, or information readily available to the public after which shall not include communications ;\n**(6)**\nin subsection (g)(3)(G)\u2014\n**(A)**\nby inserting Tribal, territorial, after State, ; and\n**(B)**\nby inserting , including those exercised under subsection (a)(2) after authorities ;\n**(7)**\nby redesignating subsections (j), (k), and (l) as subsections (k), (l), and (m);\n**(8)**\nby striking subsection (i) and inserting the following:\n(i) Applicability of other laws to activities related to the mitigation of threats from unmanned aircraft systems or unmanned aircraft Sections 32, 1030, and 1367 and chapters 119 and 206 of title 18, United States Code, and section 46502 of title 49, United States Code, may not be construed to apply to activities of the Coast Guard, whether under this section or any other provision of law, that\u2014 (1) are conducted outside the United States; and (2) are related to the mitigation of threats from unmanned aircraft systems or unmanned aircraft. (j) Terminations (1) Counter-UAS authority The authority to carry out this section with respect to a covered facility or asset, protecting the public, and enforcing the law shall terminate on September 30, 2031. (2) State, local, tribal, and territorial law enforcement and correctional agencies Authority of State, local, tribal, and territorial law enforcement and correctional agencies under subsection (a)(2) shall terminate on December 31, 2031. ;\n**(9)**\nin subsection (l), as so redesignated\u2014\n**(A)**\nin paragraph (3)(C) by inserting a Federal law enforcement, correctional, and homeland security agency mission necessary to enforce the law, protect the public or to after directly relates to ;\n**(B)**\nby striking paragraph (6) and inserting the following:\n(6) (A) For purposes of subsection (a)(1), the term personnel means officers, employees, contractors, detailed personnel, and deputized personnel who perform Federal law enforcement, correctional, homeland or national security duties. (B) For purposes of subsection (a)(2), the term personnel means officers and employees of State, local, Tribal, and territorial law enforcement and correctional agencies. ; and\n**(C)**\nby adding at the end the following:\n(9) The term correctional facility means any jail, prison, or any other penal or detention facility operated by a State, local, Tribal, or territorial law enforcement agency, or by a private party that is under contract with a State, local, Tribal, or territorial law enforcement agency, and used to house individuals who have been arrested, detained, held, or charged with or convicted of criminal offenses. (10) The term critical infrastructure has the meaning given the term in subsection (e) of the Critical Infrastructures Protection Act of 2001 ( Public Law 107\u201356 ). ; and\n**(10)**\nby adding at the end the following:\n(n) Reimbursement program Not later than 180 days of after the date of enactment of the SAFER SKIES Act , the Secretary of Homeland Security and the Attorney General shall provide the appropriate congressional committees with a plan to establish a reimbursement program for Federal agencies providing counter-UAS protection to events that are not organized or operated by the Federal Government. .\n#### 3. Use of grant funds for unmanned aircraft and counter unmanned aircraft systems\nSection 501(a)(1) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10152(a)(1) ) is amended by adding at the end the following:\n(J) Programs to purchase and operate unmanned aircraft systems (as defined in section 44801 of title 49, United States Code) to benefit public safety. (K) Programs to purchase and operate counter-UAS systems (as defined in section 44801 of title 49, United States Code) included on the list of technologies established by subsection (d)(2)(A)(iii) section 210G of the Homeland Security Act of 2002 ( 6 U.S.C. 124n(d)(2)(A)(iii) ) to exercise the authority granted under subsection (a)(2) of such section. .\n#### 4. Use of grant funds for unmanned aircraft\nSection 1701(b) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10381(b) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (23) and (24) as paragraphs (24) and (25), respectively;\n**(2)**\nby inserting after paragraph (22) the following:\n(23) to purchase and operate unmanned aircraft systems (as such term is defined in section 44801 of title 49, United States Code) to benefit public safety; ; and\n**(3)**\nin paragraph (24), as so redesignated, by striking (22) and inserting (23) .\n#### 5. Penalties\n##### (a) Definition\nIn this section, the term unmanned aircraft has the meaning given the term in section 44801 of title 49, United States Code.\n##### (b) Felony penalty for repeat violation of national defense airspace\nSection 46307 of title 49, United States Code, is amended by adding at the end the following: If a person is convicted of a second or subsequent offense under this section, the punishment shall be imprisonment for not more than 5 years, a fine under title 18, or both. .\n##### (c) Increased penalties for operation of unmanned aircraft To facilitate felony offense\nIf a person who is convicted of a felony offense (other than an offense based solely on the operation of an unmanned aircraft) knowingly operated an unmanned aircraft during, in relation to, or in furtherance of such offense, the maximum imprisonment otherwise provided by law for that offense shall be doubled or increased by 5 years, whichever is less.\n##### (d) Increased penalties for use of unmanned aircraft to introduce contraband into prisons\nIf a defendant who is convicted under section 1791 of title 18, United States Code, knowingly used an unmanned aircraft to provide a prohibited object to an inmate of a prison, the maximum imprisonment otherwise provided by law for that offense shall be increased by 5 years.\n##### (e) Directive to United States Sentencing Commission: enhanced sentencing range for use of unmanned aircraft\n**(1) In general**\nTo carry out the purposes of this section, during the Sentencing Commission\u2019s amendment cycle in progress at the time this Act is enacted, the Commission shall, under section 994 of title 28, United States Code\u2014\n**(A)**\npromulgate guidelines, or amendments to guidelines, that substantially increase the sentencing range for all offenses involving the use of an unmanned aircraft; and\n**(B)**\nas necessary, promulgate policy statements, or amendments to policy statements to assist in the application of this section.\n**(2) Enhanced penalties**\nIn any case in which the enhanced penalties of subsection (c) apply, the guidelines and amendments issued under paragraph (1) shall call for an increase of at least 6 levels in the base offense level and in all other cases, the base offense level shall be increased by at least 4 levels.\n##### (f) Penalties for unauthorized counter-UAS actions\nAny entity or individual authorized to take such actions to mitigate the threat posed by an unmanned aircraft system or unmanned aircraft pursuant to section 210G of the Homeland Security Act of 2002 ( 6 U.S.C. 124n ) who knowingly engages in such actions without Federal coordination as required by those statutes, shall be subject to\u2014\n**(1)**\na civil fine up to $100,000 per violation; or\n**(2)**\nsuspension of counter-UAS authority pending review by the Attorney General or Secretary of Homeland Security.\n##### (g) Civil enforcement\nThe Attorney General is authorized to bring a civil action in a United States district court to collect fines and enforce civil penalties imposed under this section.\n##### (h) Effective date\nThis section and the amendments made by this section shall take effect 30 days after enactment of this Act.\n#### 6. Rulemaking and implementation\n##### (a) Rulemaking authority\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Secretary of Homeland Security and the Attorney General, in coordination with the Secretary of Defense and the Secretary of Transportation, shall develop and publish regulations governing counter-UAS authority for SLTT law enforcement agencies and correctional agencies under this Act and the amendments made by this Act.\n**(2) Role of FAA**\nIn carrying out the rulemaking in paragraph (1), the Secretary of Homeland Security and the Attorney General shall coordinate with the Administrator of the Federal Aviation Administration on any aspect of the rulemaking that affects aviation safety, civilian aviation and aerospace operations, aircraft airworthiness, or the use of airspace.\n**(3) Saving clause**\nNothing in this section shall be construed to vest in the Secretary or the Attorney General any authority of the Secretary of Transportation or the Administrator of the Federal Aviation Administration.\n**(4) Authorized equipment and technology**\nThe Secretary of Homeland Security, the Attorney General, the Secretary of Defense, in coordination with the Administrator of the Federal Aviation Administration, the Chairman of the Federal Communications Commission, and the Administrator of National Telecommunications and Information Administrator shall authorize equipment and technology to be used for actions in subparagraphs (B), (C), (D), and (F) of section 210G(b)(1) of the Homeland Security Act of 2002.\n##### (b) Training and compliance\n**(1) In general**\nThe Attorney General, in coordination with the Secretary of Homeland Security, the Secretary of Defense, and the Department of Transportation, shall approve standards for training programs for SLTT law enforcement agencies or correctional agencies for the safe and lawful interception of drones. Such training programs shall include instruction on the legal, operational, and technological aspects of counter-UAS operations.\n**(2) Compliance audits**\nThe Attorney General and the Secretary of Homeland Security shall periodically conduct compliance audits to prevent misuse of counter-UAS authority.\n##### (c) Definitions\nIn this section:\n**(1) SLTT law enforcement agency**\nThe term SLTT law enforcement agency means a State, local, Tribal, or territorial law enforcement agency.\n**(2) Correctional agency**\nThe term correctional agency means a Federal, State, local, Tribal, or territorial government body responsible for operating correctional facilities or a private party that is under contract with a State, local, Tribal, or territorial law enforcement agency to operate such facilities.\n**(3) Correctional facility**\nThe term correctional facility means any jail, prison, or any other penal or detention facility operated by a State, local, Tribal, or territorial law enforcement agency, or by a private party that is under contract with a State, local, Tribal, or territorial law enforcement agency, and used to house individuals who have been arrested, detained, held, or charged with or convicted of criminal offenses.\n#### 7. Severability\nIf any provision of this Act, or the application of any provision of this Act to any person or circumstance is held invalid, the application of such provision or circumstance and the remainder of this Act shall not be affected thereby.",
      "versionDate": "2025-12-15",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-12-18",
        "text": "Became Public Law No: 119-60."
      },
      "number": "1071",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
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
        "updateDate": "2026-01-09T16:21:12Z"
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
      "date": "2025-12-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3481is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "SAFER SKIES Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-08T06:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAFER SKIES Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-08T06:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to expand the authority to use counter-unmanned aircraft system technologies to State, local, Tribal, and territorial law enforcement and correctional agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-08T06:03:16Z"
    }
  ]
}
```
