# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4695?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4695
- Title: Facial Recognition Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4695
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-03-17T08:05:49Z
- Update date including text: 2026-03-17T08:05:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4695",
    "number": "4695",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "L000582",
        "district": "36",
        "firstName": "Ted",
        "fullName": "Rep. Lieu, Ted [D-CA-36]",
        "lastName": "Lieu",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Facial Recognition Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-17T08:05:49Z",
    "updateDateIncludingText": "2026-03-17T08:05:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:10:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-23T14:10:30Z",
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
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MD"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4695ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4695\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Lieu (for himself, Ms. Clarke of New York , Mr. Gomez , Mr. Ivey , and Mr. Veasey ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Science, Space, and Technology , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo regulate law enforcement use of facial recognition technology, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Facial Recognition Act of 2025 .\n#### 2. Ineligibility for certain funds\nIn the case of a State or unit of local government that received a grant award under subpart 1 of part E of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 42 U.S.C. 3750 et seq. ), if the State or unit of local government fails to substantially to comply with the requirements under this Act for a fiscal year, the Attorney General shall reduce the amount that would otherwise be awarded to that State or unit of local government under such grant program in the following fiscal year by 15 percent.\n#### 3. Definitions\nIn this Act:\n**(1) Arrest photo database**\nThe term arrest photo database means a database populated primarily by booking or arrest photographs or photographs of persons encountered by an investigative or law enforcement officer.\n**(2) Candidate list**\nThe term candidate list means the top images that a facial recognition system determines to most closely match a probe image.\n**(3) Derived**\nThe term derived means that a Federal or State government would not have possessed the information or evidence but for the use of facial recognition, regardless of any claim that the information or evidence is attenuated from such recognition, and would inevitably have been discovered or obtained the information or evidence through other means.\n**(4) Facial recognition**\nThe term facial recognition means an automated or semi-automated process that assists in identifying or verifying an individual or captures information about an individual based on the physical characteristics of an individual\u2019s face, head or body, or that uses characteristics of an individual\u2019s face, head or body, to infer emotion, associations, activities, or the location of an individual.\n**(5) Face surveillance**\nThe term face surveillance means the use of facial recognition with real-time or stored video footage to track, observe, or analyze the movements, behavior, data, or actions of an individual or groups of individuals.\n**(6) Illegitimately obtained information**\nThe term illegitimately obtained information means personal data or information that was obtained\u2014\n**(A)**\nin a manner that violates Federal, State, or Tribal law;\n**(B)**\nin a manner that violates a service agreement between a provider of an electronic communication service to the public or a provider of a remote computing service and customers or subscribers of that provider;\n**(C)**\nin a manner that is inconsistent with the privacy policy of a provider described in subparagraph (B), if applicable;\n**(D)**\nby deceiving a person whose information was obtained;\n**(E)**\nthrough the unauthorized access of an electronic device or online account;\n**(F)**\nin violation of a contract, court settlement, or other binding legal agreement; or\n**(G)**\nfrom unlawful or unconstitutional practices by any government official or entity.\n**(7) Investigative or law enforcement officer**\nThe term investigative or law enforcement officer means\u2014\n**(A)**\nany officer of a State or a political subdivision thereof, or of the United States, who is empowered by law to conduct investigations of or to make arrests for civil or criminal offenses or violations of Federal or State law and any attorney authorized by law to prosecute or participate in the prosecution of such offenses; and\n**(B)**\ndoes not include any officer, employee, or contractor of a State department of motor vehicles.\n**(8) Law enforcement agency**\nThe term law enforcement agency means any agency of the United States authorized to engage in or supervise the prevention, detection, investigation, or prosecution of any violation of civil or criminal law.\n**(9) Probe image**\nThe term probe image means an image of a person that is searched against a database of known, identified persons or an unsolved photo file.\n**(10) Prosecutor**\nThe term prosecutor means the principal prosecuting attorney of a State or any political subdivision thereof and any attorney for the Government (as such term is defined for the purposes of the Federal Rules of Criminal Procedure).\n**(11) Operational testing**\nThe term operational testing means testing that evaluates a complete facial recognition system as it is used in the field, including measuring false positive and false negative error rates for field uses of the system on operational or operationally representative data and under the environmental conditions and technical product settings and configurations typically used, as well as assessing the variability of system use by different users.\n**(12) Reference photo database**\nThe term reference photo database means a database populated with photos of individuals that have been identified, including databases composed of driver\u2019s licenses, passports, or other documents made or issued by or under the authority of the United States Government, a State, a political subdivision thereof, databases operated by third parties, and arrest photo databases.\n**(13) State**\nThe term State means each State of the United States, the District of Columbia, the Commonwealth of Puerto Rico, the Virgin Islands, American Samoa, Guam, and the Northern Mariana Islands.\nI\nUse of facial recognition by Law Enforcement\n#### 101. Facial recognition\n##### (a) Reference photo databases\n**(1) In general**\nAn investigative or law enforcement officer may only use or request facial recognition in conjunction with a reference photo database pursuant to an order issued under subsection (b) and the emergencies and exceptions under subsection (c).\n**(2) Maintenance**\n**(A) In general**\nBeginning on 180 days after the date of the enactment of this Act, and every six months thereafter, with respect to an arrest photo database used in conjunction with facial recognition, the custodian of such arrest photo database shall remove from such database all photos of each person who\u2014\n**(i)**\nhas not attained 18 years of age;\n**(ii)**\nhas been released without a charge;\n**(iii)**\nhas been released after charges are dropped or dismissed; or\n**(iv)**\nwas acquitted of the charged offense.\n**(B) Rule of construction**\nNothing in this paragraph shall be construed to prohibit an investigative or law enforcement officer from using a database for other investigative procedures, such as finger printing, and shall only apply to the use of a reference photo database for the use of facial recognition.\n**(3) Procedures**\nAny agency responsible for maintaining and operating an arrest photo database shall establish procedures to ensure compliance with paragraph (3).\n##### (b) Orders\n**(1) Approval**\nAn application for a warrant to use a reference photo database may not be submitted for consideration by a court unless the head of a law enforcement agency (or a designee) approves such an application.\n**(2) Authority**\nExcept as provided by subsection (d), the principal prosecutor of a State or any political subdivision thereof and any attorney for the Government (as such term is defined for the purposes of the Federal Rules of Criminal Procedure), may make an application to a court of competent jurisdiction for, in conformity with paragraph (3), an order authorizing the use of facial recognition in conjunction with a reference photo database within the jurisdiction of that judge.\n**(3) Application**\nExcept as provided in subsection (c), a court of competent jurisdiction may issue an order authorizing the use of facial recognition in conjunction with a reference photo database if a prosecutor submits an application to that court that establishes the following:\n**(A)**\nThe identity of the investigative or law enforcement officer making the application, and the officer authorizing the application.\n**(B)**\nAs full and complete a description as possible of the person that the officer seeks to identify.\n**(C)**\nThe photos or video portraying the person that will be used to search the reference photo database.\n**(D)**\nAny details regarding other investigative measures taken to identify such person and an explanation for why such measures failed or are reasonably unlikely to succeed.\n**(E)**\nAny other investigative procedures to identify such person have been tried and failed or are reasonably unlikely to succeed.\n**(F)**\nProbable cause to believe that such person has committed or is committing a particular offense or offenses enumerated in section 3559(c)(2)(F) of title 18, United States Code.\n**(4) Contents of order**\nThe order described in this paragraph shall include the following:\n**(A)**\nAll information required to be included in the application pursuant to such paragraph (3).\n**(B)**\nA prohibition on the use, for purposes of a search of a reference photo database, other than pursuant to another order under this Act, of any photo or video not specifically listed in the order.\n**(C)**\nA time period within which the search shall be made not more than 7 days, and after which no such search may be made, except pursuant to another order under this Act.\n**(D)**\nThe authority under which the search is to be made.\n**(5) Notice to the Public**\n**(A) In general**\nEach State department of motor vehicles shall post notices in conspicuous locations at each department office, make written information available to all applicants at each office, and provide information on the department website regarding State investigative or law enforcement officers\u2019 searches of driver\u2019s license and ID photos through facial recognition. The notices, written information, and online information must describe how officers use and access facial recognition in criminal investigations.\n**(B) Language requirement**\nNotices required under subparagraph (A) shall be posted, as necessary and reasonable, in Spanish or any language common to a significant portion of the department\u2019s customers, if they are not fluent in English. The department shall provide translations of the poster and an electronic link that leads to the department\u2019s website upon request.\n**(6) Conforming Amendments**\nSection 2721 of title 18, United States Code, is amended\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nin paragraph (1), by striking the or at the end;\n**(ii)**\nin paragraph (2), by striking the period at the end and inserting ; or ; and\n**(iii)**\nby inserting after paragraph (2) the following:\n(3) a department operated facial recognition system, except as provided in subsection (f) of this section. ;\n**(B)**\nin subsection (b)(1), by inserting before the period at the end the following: but if the personal information or highly restricted personal information to be disclosed is a person\u2019s photograph to be used or enrolled in a law enforcement facial recognition system, only on a case-by-case basis that does not involve the bulk transfer of persons\u2019 photographs to a State or Federal law enforcement agency or a qualified third party entity that will allow law enforcement to access those photographs for the purposes of facial recognition ; and\n**(C)**\nby adding at the end the following:\n(f) Law enforcement access to facial recognition systems A State department of motor vehicles, and any officer, employee, or contractor thereof, may make available a department-operated facial recognition system to a State or Federal law enforcement agency, or perform searches of such a system on behalf of the agency, only pursuant to an order issued under section 101 of the Facial Recognition Act of 2025 . .\n##### (c) Emergencies and exceptions\n**(1) Initial use**\nNotwithstanding subsections (a) and (b), an investigative or law enforcement officer may use or request facial recognition in conjunction with a reference photo database\u2014\n**(A)**\nto assist in identifying any person who is deceased, incapacitated or otherwise physically unable of identifying himself, or the victim of a crime, whom the officer determines, in good faith, cannot be identified through other means;\n**(B)**\nto assist in identifying a person whom the officer believes, in good faith, is the subject of an alert through an AMBER Alert communications network, as that term is used in section 301 of the Prosecutorial Remedies and Other Tools to end the Exploitation of Children Today Act of 2003 ( 34 U.S.C. 20501 );\n**(C)**\nto assist in identifying any person who has been lawfully arrested, during the process of booking that person after an arrest or during that person\u2019s custodial detention; or\n**(D)**\nto assist in identifying any person\u2014\n**(i)**\nif the appropriate prosecutor determines that an emergency situation exists\u2014\n**(I)**\nthat involves immediate danger of death or serious physical injury to any person; or\n**(II)**\nthat requires the use of facial recognition in conjunction with a reference photo database to occur before an order authorizing such use can, with due diligence, be obtained; and\n**(ii)**\nthere are grounds upon which an order could be entered under this section to authorize such use.\n**(2) Subsequent authorization**\nIf an investigative or law enforcement officer uses facial recognition pursuant to paragraph (1)(D), the prosecutor shall apply for an order approving the use under subsection (b) within 12 hours after the use occurred. The use shall immediately terminate when the application for approval is denied, or in the absence of an application, within 12 hours. In cases where an order is not obtained or denied, the officer shall destroy all information obtained as a result of the search.\n**(3) Affidavit required**\nWith respect to use of facial recognition pursuant to paragraph (1)(D), an appropriate prosecutor shall submit an affidavit to the court identifying specific details on why they believe that an emergency situation under clause (i) exists.\n##### (d) State law preserved\nThe authorities provided by subsections (b) and (c) do not authorize access reference photo databases maintained by a State, or a political subdivision of a State, unless State law expressly and unambiguously authorizes an investigative or law enforcement officer to\u2014\n**(1)**\naccess driver\u2019s license and identification document photos; and\n**(2)**\nuse facial recognition to conduct searches of those photos.\n#### 102. Civil rights and civil liberties\n##### (a) In general\nAn investigative or law enforcement officer may not\u2014\n**(1)**\nuse facial recognition to create a record describing how any individual exercises rights guaranteed by the Constitution, including free assembly, association, and speech;\n**(2)**\nrely on actual or perceived race, ethnicity, national origin, religion, disability, gender, gender identity, or sexual orientation in selecting which person to subject to facial recognition, except when there is trustworthy information, relevant to the locality and time frame, in the context of a particular area and for a particular period of time, that links a person with a particular characteristic described in this subsection to an identified criminal incident or scheme; or\n**(3)**\nuse facial recognition to enforce the immigration laws of the United States or share facial recognition data with other agencies for the purposes of enforcing the immigration laws of the United States.\n##### (b) Prohibition on use with body cameras\nAny investigative or law enforcement officer may not use or request facial recognition in conjunction with any image obtained from a body camera worn by that or any other officer, dashboard camera, or any aircraft camera, including a drone.\n##### (c) Prohibition on certain facial recognition\nAny investigative or law enforcement officer may not use or request facial recognition for the purpose of face surveillance.\n##### (d) Ensuring corroboration and preventing over reliance on matches\nA facial recognition match may not be the sole basis upon which probable cause is established for a search, arrest, or other law enforcement action. Any investigative and law enforcement officers using information obtained from the use of facial recognition shall examine results with care and consider the possibility that matches could be inaccurate.\n##### (e) Prohibition on illegitimately obtained information\nAn investigative or law enforcement office may not use facial recognition in conjunction with a database that contains illegitimately obtained information.\n#### 103. Logging of searches\nA law enforcement agency whose investigative or law enforcement officers use facial recognition shall log its use of the facial recognition to the extent necessary to comply with the public reporting and audit requirements of sections 104 and 105 of this Act.\n#### 104. Reporting\n##### (a) State reporting required\n**(1) State judiciary**\nNot later than the last day of the first January after the date of the enactment of this Act, and each January thereafter, each State judge who has issued a court order authorizing or approving facial recognition in conjunction with a reference photo database shall report to a State agency (as determined by the chief executive of the State) the following information:\n**(A)**\nThe number of orders or extensions was applied for.\n**(B)**\nWhether the order or extension was issued pursuant to section 101(b) or section 102(c).\n**(C)**\nWhether the order or extension was granted as applied for, was modified, or was denied.\n**(D)**\nThe offense specified in the order or application, or extension of an order.\n**(E)**\nThe identity of the applying investigative or law enforcement officer and agency making the application and the person authorizing the application.\n**(F)**\nFor orders issued pursuant to section 101(c), the reference photo database that was searched.\n**(2) Prosecutors**\nNot later than the last day of the first January after the date of the enactment of this Act, and each January thereafter, each State prosecutor, or a prosecutor of a political subdivision thereof, who has requested a court order authorizing or approving facial recognition in conjunction with a reference photo database shall report to a State agency (as determined by the chief executive of the State) the following information with respect to the use of facial recognition in conjunction with an reference photo database:\n**(A)**\nThe number of such searches run.\n**(B)**\nThe offenses that those searches were used to investigate, and for each offense, the number of searches run.\n**(C)**\nThe arrests that such searches contributed to, and the offenses for which the arrests were made, disaggregated by race, ethnicity, gender, and age.\n**(D)**\nThe number of convictions that such searches contributed to and the offenses for which the convictions were obtained, disaggregated by race, ethnicity, gender, and age.\n**(E)**\nThe number of motions to suppress made with respect to those searches, and the number granted or denied.\n**(F)**\nThe types and names of databases that were used and the number of photos removed with respect to arrest photo databases that were confirmed to have been removed in accordance with this section.\n**(3) Report to Bureau of Justice Assistance**\nNot later than 90 days after such report is submitted under paragraph (1), and annually thereafter, the State agency shall report the information collected under paragraph (1) to the Director of the Bureau of Justice Assistance.\n**(4) Report to Administrative Office of the United States Courts**\nNot later than 90 days after such report is submitted under paragraph (2), and annually thereafter, the State agency shall report the information collected under paragraph (2) to the Director of the Administrative Office of the United States Courts.\n##### (b) Federal reporting required\nNot later than the last day of the first January after the date of the enactment of this Act, and each January thereafter\u2014\n**(1)**\neach Federal judge who has issued a court order authorizing or approving facial recognition in conjunction with a reference photo database shall submit to the Director of the Administrative Office of the United States Courts a report including the information under subparagraphs (A) through (F) of subsection (a)(1); and\n**(2)**\nand a Federal prosecutor who requested such order, shall submit to the Director of the Administrative Office of the United States Courts a report including the information under subparagraphs (A) through (G) of subsection (a)(2).\n##### (c) Public reporting\nIn June of each year the Director of the Administrative Office of the United States Courts shall release to the public, post online, and transmit to the Congress a full and complete report concerning the use of facial recognition in conjunction with reference photo databases, including the information reported to the Director pursuant to subsections (a) and (b).\n##### (d) Rules\nThe Director of the Bureau of Justice Assistance and the Director of the Administrative Office of the United States Courts shall issue rules with respect to the content and form of the reports required to be filed under subsections (a) through (c) of this section and sections 105 and 106 of this Act.\n#### 105. Audits\n##### (a) Federal level audit\n**(1) In general**\nAny Federal law enforcement agency whose investigative or law enforcement officers use facial recognition, regardless of whether they use a system operated by that agency or another agency, shall annually submit data with respect to their use of facial recognition for audit by the Government Accountability Office to prevent and identify misuse and to ensure compliance with sections 101, 102, and 103 of this Act, including\u2014\n**(A)**\na summary of the findings of the audit, including the number and nature of violations identified; and\n**(B)**\ninformation about the procedures used by the law enforcement agency to remove arrest photos from databases in accordance with this Act.\n**(2) Suspension**\n**(A) In general**\nIf a violation is uncovered by the audit conducted under paragraph (1), the Federal law enforcement agency shall cease using facial recognition until such time that all violations have been corrected.\n**(B) Public notice**\nIf use of facial recognition is suspended pursuant to subparagraph (A), the Federal law enforcement agency shall notify the public of such suspension.\n##### (b) State level audit\n**(1) In general**\nAny State or local law enforcement agency whose investigative or law enforcement officers use facial recognition, regardless of whether they use a system operated by that agency or another agency, shall annually submit data with respect to their use of facial recognition to an independent State agency (as determined by the chief executive of the State) to prevent and identify misuse and to ensure compliance with sections 101, 102, and 103 of this Act. Such independent State agency shall report\u2014\n**(A)**\na summary of the findings of the audit, including the number and nature of violations identified, to Director of the Administrative Office of the United States Courts, and subsequently release that information to the public and post it online;\n**(B)**\ninformation about the procedures used by the law enforcement agency to remove arrest photos from databases in accordance with this section; and\n**(C)**\nany violations identified by the independent State agency.\n**(2) Suspension**\n**(A) In general**\nIf a violation is uncovered by the audit conducted under paragraph (1), the State or local law enforcement agency shall cease using facial recognition until such time that all violations have been corrected.\n**(B) Public notice**\nIf use of facial recognition is suspended pursuant to subparagraph (A), the State or local law enforcement agency shall notify the public of such suspension.\n##### (c) Disaggregated data\nData collected pursuant to subsection (a) or (b) shall, when feasible, be collected in a manner that allows such data to be disaggregated by race, ethnicity, gender, and age.\n#### 106. Accuracy and bias testing\n##### (a) Benchmark testing\nNo investigative or law enforcement officers may use a facial recognition system or information derived from it unless that system is annually submitted to the National Institute of Standards and Technology\u2019s benchmark facial recognition test for law enforcement to determine\u2014\n**(1)**\nthe accuracy of the system; and\n**(2)**\nwhether the accuracy of the system varies significantly on the basis of race, ethnicity, gender or age.\n##### (b) Benchmark testing for new systems\nNo investigative or law enforcement officers may begin using a new facial recognition system or information derived from it unless that system is first submitted to independent testing to determine\u2014\n**(1)**\nthe accuracy of the system; and\n**(2)**\nwhether the accuracy of the system varies significantly on the basis of race, ethnicity, gender, or age.\n##### (c) Prohibition\nAny investigative or law enforcement officer may not use facial recognition that has not achieved a sufficiently high level of accuracy, including in terms of overall accuracy and variance on the basis of race, ethnicity, gender, or age, as determined by the National Institute of Standards and Technology, on its annual benchmark test for law enforcement use.\n##### (d) Operational testing\nNo investigative or law enforcement agencies may use a facial recognition system or information derived from it unless that system is annually submitted to operational testing conducted by an independent entity, in accordance with National Institute of Standards and Technology\u2019s training protocol for operational testing, to determine\u2014\n**(1)**\nthe accuracy of the system;\n**(2)**\nthe impact of human reviewers on system accuracy; and\n**(3)**\nwhether the accuracy of the system varies significantly on the basis of race, ethnicity, gender, or age.\n##### (e) Reporting\nA summary of the findings of the tests required by subsection (a) or (d) shall be submitted to the Director of the Administrative Office of the United States Courts and posted on the internet website of the Administrative Office of the United States Courts.\n##### (f) Rulemaking required\nThe Assistant Attorney General of the Department of Justice Civil Rights Division shall issue a rule that establishes what is a sufficiently high level of accuracy for a facial recognition system used by law enforcement, including in terms of overall accuracy and variance on the basis of race, ethnicity, gender, and age. The Assistant Attorney General of the Department of Justice Civil Rights Division shall consult with outside experts in civil rights, civil liberties, racial justice, data privacy, bioethics, law enforcement, public defense, and forensic science and other relevant areas of expertise in drafting the proposed rule.\n##### (g) Effective date\nThis section shall take effect 18 months after the date of enactment of this Act.\n#### 107. Enforcement\n##### (a) Suppression\nIn the case that the use of facial recognition has occurred, no results from the use and no evidence derived therefrom may be received in evidence in any trial, hearing, or other proceeding in or before any court, grand jury, department, officer, agency, regulatory body, legislative committee, or other authority of the United States, a State, or a political subdivision thereof if the use of facial recognition violated this Act or if the use was conducted in an emergency under section 101 and the officer or agency did not subsequently obtain an order for that use as required under such section.\n##### (b) Administrative Discipline\nIf a court or law enforcement agency determines that an investigative or law enforcement officer has violated any provision of this Act, and the court or agency finds that the circumstances surrounding the violation raise serious questions about whether or not the officer acted intentionally with respect to the violation, the agency shall promptly initiate a proceeding to determine whether disciplinary action against the officer is warranted.\n##### (c) Civil action\n**(1) In General**\nAny person who is subject to identification or attempted identification through facial recognition in violation of this Act may bring a civil action in the appropriate court to recover such relief as may be appropriate from the investigative or law enforcement officer or the State or Federal law enforcement agency which engaged in that violation.\n**(2) Relief**\nIn an action under this subsection, appropriate relief includes\u2014\n**(A)**\nsuch preliminary and other equitable or declaratory relief as may be appropriate;\n**(B)**\ndamages under paragraph (3) and punitive damages in appropriate cases; and\n**(C)**\na reasonable attorney\u2019s fee and other litigation costs reasonably incurred.\n**(3) Computation of Damages**\nThe court may assess as damages whichever is the greater of\u2014\n**(A)**\nany profits made with respect to the violation suffered by the plaintiff; or\n**(B)**\n$50,000 for each violation.\n**(4) Defense**\nA good faith reliance on\u2014\n**(A)**\na court warrant or order, a grand jury subpoena, a legislative authorization, or a statutory authorization; or\n**(B)**\na good faith determination that section 101 permitted the conduct complained of,\nis a complete defense against any civil action brought under this Act.\n**(5) Limitation**\nA civil action under this section may not be commenced later than two years after the date upon which the claimant first has a reasonable opportunity to discover the violation.\n##### (d) Civil action for disparate impact\nAn individual may bring a civil action when use of facial recognition or face surveillance by a law enforcement agency, or any technological element, criteria, method, or design feature thereof acting individually or in concert, results in disparate treatment or adverse impact against an individual or class of individuals on the basis of race, ethnicity, gender, or age.\n#### 108. Notice requirement\n##### (a) Notice requirement\nA law enforcement agency that uses facial recognition to attempt to identify an individual who is arrested shall, at minimum, provide to the individual\u2014\n**(1)**\na notice of\u2014\n**(A)**\nthe name the law enforcement agency that operated the facial recognition system used; and\n**(B)**\nthe name of the database, if any, that was used to identify the individual; and\n**(2)**\na copy of\u2014\n**(A)**\nthe order that authorized the use of facial recognition;\n**(B)**\naccuracy or bias reports required under this Act;\n**(C)**\neach probe image that was used by the agency;\n**(D)**\nany modifications made to the probe image;\n**(E)**\nthe candidate list, in rank order, produced by the facial recognition system; and\n**(F)**\nany other police documentation related to the use of facial recognition in the law enforcement investigation.\n##### (b) Language requirement\nThe information required under subsection (a) shall be provided to such individual in an appropriate language for such individual if the individual is not fluent or literate in English.\nII\nCertain requirements and limitations on facial recognition systems and research\n#### 201. National Institute for Standards and Technology assistance\n##### (a) In general\nThe National Institute of Standards and Technology (hereinafter in this section referred to as NIST ) shall\u2014\n**(1)**\ndevelop best practices for law enforcement agencies to evaluate the accuracy and fairness of their facial recognition systems;\n**(2)**\ndevelop and offer an ongoing benchmark facial recognition test for law enforcement that\u2014\n**(A)**\nconducts evaluations of actual algorithms used by law enforcement agencies;\n**(B)**\nuses the types of probe images, including in terms of quality, actually used by law enforcement agencies in its testing;\n**(C)**\nevaluates algorithms on larger databases that reflect the size of databases actually used by law enforcement; and\n**(D)**\nevaluates whether the accuracy of a facial recognition algorithm varies on the basis of race, ethnicity, gender, or age and assessments of bias in facial recognition systems;\n**(3)**\ndevelop an operational testing protocol that independent testers and law enforcement agencies may implement for annual operational testing to determine\u2014\n**(A)**\nthe accuracy of the facial recognition system;\n**(B)**\nthe impact of human reviewers on facial recognition system accuracy; and\n**(C)**\nwhether the accuracy of the facial recognition system varies significantly on the basis of race, ethnicity, gender, or age; and\n**(4)**\nstudy and develop training standards for human operators reviewing the results of facial recognition searches to ensure accuracy and prevent bias.\n##### (b) Authorization of appropriations\nThere is authorized to be appropriated to the National Institute of Standards and Technology to carry out subsection (a) $5,000,000 for each of the fiscal years 2026 through 2029.\n#### 202. Rule of construction with respect to State and local privacy protections\n##### (a) Rule of construction\nNothing in this Act shall be construed to preempt concurrent or more stringent limitations on the use of facial recognition, or any other privacy, civil rights, and civil liberties laws and rules, by the Federal Government, a State, or a political subdivision of a State.\n##### (b) Use of facial recognition\nNothing in this Act shall be construed to authorize the use of facial recognition by a State, or a political subdivision of a State, unless the laws of that State or political subdivision expressly and unambiguously authorizes such use.\n#### 203. Policy on use of facial recognition systems required\nNot later than 90 days after the date of the enactment of this Act, each agency covered by this statute shall establish and make publicly available on the internet website of such agency a policy governing the agency\u2019s use of facial recognition systems to ensure investigative or law enforcement officer compliance with the requirements of this Act.\n#### 204. Limitation on liability\nA State shall not be immune under the eleventh amendment to the Constitution of the United States from an action in Federal or State court of competent jurisdiction for a violation of this Act. In any action against a State for a violation of the requirements of this Act, remedies (including remedies both at law and in equity) are available for such a violation to the same extent as such remedies are available for such a violation in an action against any public or private entity other than a State.",
      "versionDate": "2025-07-23",
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
        "updateDate": "2025-09-17T16:57:31Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4695ih.xml"
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
      "title": "Facial Recognition Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Facial Recognition Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To regulate law enforcement use of facial recognition technology, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:33:22Z"
    }
  ]
}
```
